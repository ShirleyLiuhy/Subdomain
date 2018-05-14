#!/usr/bin/env python
# -*-coding:utf-8 -*-

from common import http_requests_get
import re

domain = 'jd.com'

class Bing(object):
    def __init__(self,domain,pages):
        self.domain = domain
        self.pages = pages
        self.result = []

    def run(self):
        for i in range(1, self.pages):
            page = (i - 1) * 10
            url = 'http://cn.bing.com/search?q=site:{}&first={}'.format(domain, page)
            res = http_requests_get(url=url)
            retext = '<cite>(.*?)<strong>'+self.domain+'</strong>'
            results = re.findall(retext, res.content)
            for i in results:
                if 'https' in i:
                    i = i.replace('https://', '')
                    sub = i + self.domain
                    self.result.append(sub)
                    # print sub
                else:
                    sub = i + self.domain
                    self.result.append(sub)
        return list(set(self.result))
        # return self.result



# print Bing(domain=domain,pages=10).run()


