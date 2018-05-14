#!/usr/bin/env python
#config:utf-8

import dns.resolver

result = dns.resolver.query('www.jd.com','A')
print result.response.answer
