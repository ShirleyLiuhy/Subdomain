#!/usr/bin/env python
# -*-coding:utf-8 -*-


from common import http_requests_get,is_domain
import re

class Crt(object):
    def __init__(self, domain):
        self.domain=domain
        self.site='http://crt.sh/?q=%25.'
        self.result=[]

    def run(self):
        url = self.site + self.domain
        print url
        try:
            r=http_requests_get(url=url)
            # self.result.append(re)
            results = re.findall('</TD>\n    <TD>(.*?)</TD>\n    <TD><A',r.content,re.S)
            for result in results:
                if is_domain(result):
                    self.result.append(result)
            return list(set(self.result))
        except Exception,e:
            return self.result