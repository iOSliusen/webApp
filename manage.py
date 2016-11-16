from flask import Flask
from flask import request

from urllib import parse
import urllib.request

import base64

try:
    import json
except ImportError:
    import simplejson as json
# 这里填上你申请到的bing的accout key 就可以了
AccountKey = 'a6gw5MVOZq0OkrcmkY8qG6+A90T0Qn67UaZBg7DD2mA'
top = 5
skip = 0
format = 'json'

#搜索主函数

def BingSearch(query):
    payload = {}
    payload['$top'] = top
    payload['$skip'] = skip
    payload['$format'] = format
    payload['Query'] = "'" + query + "'"

    url = 'https://api.datamarket.azure.com/Bing/Search/Web?' + parse.urlencode(payload)
    sAuth = 'Basic ' + base64.b64encode((':' + AccountKey).encode('utf-8')).decode()

    headers = {}
    headers['Authorization'] = sAuth
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        the_page = response.read()

        # print(the_page.decode())

        # data = json.loads(the_page.decode())#解析json数据
        data = the_page.decode()

        return data
    except Exception as e:
        print(e)


app = Flask(__name__)#创建flask实例

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/getInfo',methods=['GET'])
def show_username():

    username   = request.args.get("username")

    data = BingSearch(username)

    return  data


if __name__ == '__main__':
    app.run()



