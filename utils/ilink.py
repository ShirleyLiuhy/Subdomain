#!/usr/bin/env python
# -*-coding:utf-8 -*-

from common import http_requsets_post,is_domain
import re

class Ilink(object):
    def __init__(self, domain):
        self.domain=domain
        self.site='http://i.links.cn/subdomain/'
        self.result=[]

    def run(self):
        try:
            url=self.site
            r=http_requsets_post(url=url,payload={'domain':self.domain,'b2':'1','b3':'1','b4':'1'})
            # self.result.append(r.content)
            results = re.findall('value="http://(.*?)"><input type=hidden',r.content)
            for result in results:
                if is_domain(result):
                    self.result.append(result)
            return list(set(self.result))
            # return self.result
        except Exception,e:
            return self.result