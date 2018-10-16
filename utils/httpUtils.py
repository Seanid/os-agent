#-*- coding:utf-8 -*-
#http请求客户端
import urllib2
import json
import sys

sys_encode=sys.getfilesystemencoding()
ua_header={"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;","Content-Type":"application/json"}

def post(url,data):
    reqdata=json.dumps(data)
    request=urllib2.Request(url=url,data=reqdata,headers=ua_header)
    response=urllib2.urlopen(request)
    return response.read().decode('UTF-8').encode(sys_encode)
    