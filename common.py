#!/usr/bin/env python
# -*-coding:utf-8 -*-
import re
import json
import requests.packages.urllib3
#https请求访问http网站不报错(disable_warnings)
requests.packages.urllib3.disable_warnings()
from config import *

import requests

#requests get请求
def http_requests_get(url):
    try:
        result = requests.get(
            url=url,
            headers=headers,
            timeout=timeout,
            allow_redirects=allow_redirects,
            # verity=allow_ssl_verify
        )
        return result
    except Exception, e:
        return requests.models.Response()
        

# result=requests.get('http://www.baidu.com')
# print result

#requests post请求
def http_requsets_post(url,payload):
	try:
		result=requests.post(
			url=url,
			data=payload,
            headers=headers,
			timeout=timeout,
			allow_redirects=allow_redirects,
			# verity=allow_ssl_verify
        )
		return result
	except Exception,e:
		return requests.models.Response()

# result=requests.post('http://www.baidu.com',data={'wd':'abc'})
# print result

def is_domain(domain):
	domain_regex=re.compile(
		r'(?:[A-Z0-9_](?:[A-Z0-9-_]{0,247}[A-Z0-9-_])?\.)+(?:[A-Z]{2,6}|[A-Z0-9-]{2,}(?<!-))\Z',
	re.IGNORECASE)
	return True if domain_regex.match(domain)else False
	



def save_result(filename,result):
    try:
        f = open(filename,'w')
        json.dump(result,f,indent=4)
    except Exception,e:
        print e


def read_json(filename):
    try:
        f = open(filename,'r')
        datas = json.load(f)
        return datas
    except Exception,e:
        print e

