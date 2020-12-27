import requests
from fake_useragent import UserAgent
import sys
from lxml import etree
import pymysql
from dbutils.pooled_db import PooledDB #pip3 install DBUtils，连接池

db_config = {
  "host": "127.0.0.1",
  "port": 3306,
  "user": "root",
  "passwd": "yuehong890313",
  "db": "testdb",
  "charset": "utf8mb4",
  "maxconnections":0,   # 连接池允许的最大连接数
  "mincached":4,        # 初始化时连接池中至少创建的空闲的链接,0表示不创建
  "maxcached":0,        # 连接池中最多闲置的链接,0不限制
  "maxusage" :5,        # 每个连接最多被重复使用的次数,None表示无限制
  "blocking":True       # 连接池中如果没有可用连接后是否阻塞等待
                        #  True 等待; False 不等待然后报错
}    

if __name__ == "__main__":
    try:
        spool = PooledDB(pymysql, **db_config) 
        conn = spool.connection()
        ua = UserAgent(verify_ssl=False)
        for i in range(1,11):
            url = f'https://movie.douban.com/top250?start={i*25}'
            header = {
                'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'#ua.random
            }
            try:
                response = requests.get(url, headers=header)
            except Exception as e:
                print('下载出现异常', e)
                sys.exit(1)
            try:
                html = etree.HTML(response.text)
                movies = html.xpath('//div[@class="hd"]')
                for movie in movies:
                    try:
                        title = movie.xpath('a/span[1]/text()')[0]
                        link = movie.xpath('a/@href')[0]
                    except Exception as e:
                        print('book error', e)
                        sys.exit(1)
                    for j in range(0,5):
                        commitUrl = f'{link}comments?start={j*20}&limit=20&status=P&sort=new_score'
                        try:
                            response = requests.get(commitUrl, headers=header)
                        except Exception as e:
                            print('下载出现异常', e)
                            sys.exit(1)
                        try:
                            html = etree.HTML(response.text)
                            comment_content = html.xpath('//div[@class="comment-item "]/div[@class="comment"]/p/span/text()')
                            starList = html.xpath('//div[@class="comment-item "]/div[@class="comment"]/h3/span[@class="comment-info"]/span[contains(@class, "rating")]/@class')
                            for idx, content in enumerate(comment_content):
                                comment = content.replace(" ","")
                                comment = content.replace("\n","")
                                comment = content.replace("\t","")
                                if len(comment) > 0:
                                    star = starList[idx].replace('allstar', '').replace('rating', '').strip() if len(starList) > idx else 0
                                    sql = "insert into index_movie (name, stars, comments) values (%s, %s , %s)"
                                    with conn.cursor() as cur:
                                        cur.execute(sql,(title,star,comment)) 
                                    conn.commit()                                              
                        except Exception as e:
                            sys.exit(1)
            except Exception as e:
                print('page error', e)
    except Exception as e:
        print('page error', e)