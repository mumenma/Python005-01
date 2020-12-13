import requests
import json
import os
from pathlib import *
import threading
import requests
from fake_useragent import UserAgent
import sys
from crawling import Engine
from crawling import Crawling


# cookie 文件。已经登录网页的 cookie 信息。
COOKIE_FILE = './cookie.txt'

# 保存结果的文件。
RESULT_FILE = './result/result.json'

# 获取答案的数量。如果为 0 则获取页面中所有的答案。
ANSWER_NUMBER = 0

# 选择答案的排序的方式。 zhihu 页面上提供了两种排序的方式。分别是 default(默认排序) 和 updated(按时间排序) 。
SORTED_BY = "default"

def fetchResult(url):
    # 发起网络请求，获取数据
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
 
    # 发起网络请求
    r = requests.get(url,headers=headers)
    r.encoding = 'Unicode'
    return r.text
 


def parseJson(text):
    json_data = json.loads(text)

    if json_data is None:
        return

    itemList = json_data['data']
    nextUrl = json_data['paging']['next']
    
    idList = []

    if not itemList:
        return None, idList
    for item in itemList:
        type = item['target']['type']
        
        if type == 'answer':
            # 回答
            question = item['target']['question']
            answer = item['target']['content']
            id = question['id']
            title = question['title']
            url = 'https://www.zhihu.com/question/' + str(id)
            # print("问题：",id,title, answer)
            # 保存到数据库
            #saveQuestionDB(str (id),title,url, answer)
            print(str(id))
            idList.append(str(id))
    # print(idList)
    return nextUrl, idList
 
 
def crawl_2(topicID, top=15):
    '''essence'''

    url = 'https://www.zhihu.com/api/v4/topics/' + topicID + '/feeds/essence?limit=' + str(top) + '&include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&offset=0'
    count = 0
    idList = []# 问题ID. www.zhihu.com 网页上对应的问题 id 值。例如：https://www.zhihu.com/question/52368821 最后的字符串
    while url and count <= 10 :
        text = fetchResult(url)
        url, addList = parseJson(text)
        for add in addList:
            if add not in idList:
                idList.append(add)
        count = count + 1
    print(idList)
    # 读取cookie
    with open(COOKIE_FILE, 'r') as rf:
        cookie = rf.read()

    # 去除重复的id
    question = (set(idList))

    # 检查配置
    if not check_config(cookie, SORTED_BY):
        return False

    # 执行
    engine = Engine(question=question, cookie=cookie, result_file=RESULT_FILE, answer_number=ANSWER_NUMBER,
                    sort_by=SORTED_BY)
    engine.run()

def check_cookie(cookie):
    """
    检查 cookie 是否可以登陆。
    :param cookie: (str) cookie
    :return: (bool)
    """
    user_agent = UserAgent(verify_ssl=False)
    headers = {
        'user-agent': user_agent.random,
        'cookie': cookie,
    }

    login_url = "https://www.zhihu.com/signup"
    response = requests.get(login_url, headers=headers, allow_redirects=False)
    if response.status_code == 302:
        return True
    print("Invalid cookie !")
    return False


def check_sort_by(sort_by):
    """
    检查爬取的排序方式。
    :param sort_by: (str) default 或 updated
    :return: (bool)
    """
    _sort = (Crawling.UPDATED, Crawling.DEFAULT)
    if sort_by not in _sort:
        print("Invalid config of SORT_BY. SORT_BY in [{}]".format(_sort))
        return False
    return True


def check_config(cookie, sort_by):
    """
    检查配置信息
    :param cookie: (str) cookie
    :param sort_by: (str) sort_by
    :return: (bool)
    """
    if not check_cookie(cookie):
        return False
    if not check_sort_by(sort_by):
        return False
    return True
 
if __name__ == '__main__':
    topicID = "20746089"  #topic id  20746089 对应的是5G手机
    crawl_2(topicID)