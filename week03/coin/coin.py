import pymysql
from dbutils.pooled_db import PooledDB #pip3 install DBUtils，连接池
import datetime

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


def trans(from_name,to_name,amount):
    try:
        spool = PooledDB(pymysql, **db_config) 
        conn = spool.connection()
        with conn.cursor() as cur:
            sqlFrom = "select user_id from user where user_name = '"+from_name+"';"
            cur.execute(sqlFrom)
            fromId = cur.fetchone()[0]
            sqlTo = "select user_id from user where user_name = '"+to_name+"';"
            cur.execute(sqlTo)
            toId = cur.fetchone()[0]
            update1 = "update balance set user_assets = user_assets - "+str(amount)+" where user_id = "+ str(fromId)
            cur.execute(update1)
            update2 =  "update balance set user_assets = user_assets + "+str(amount)+" where user_id = " + str(toId)
            cur.execute(update2)
            create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            insert = "insert into trans values(%s,%s,%s,%s)"
            cur.execute(insert,(create_time,fromId,toId,amount))
        conn.commit()
    except Exception as e:
        print(f"insert error {e}")


if __name__ == "__main__":
    trans("张三","李四",100)