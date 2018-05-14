#!/usr/bin/env python
#config:utf-8

from utils.ilink import Ilink
from utils.crt import Crt
from utils.brutedns import BruteDns
from utils.baidusite import BaiduSite
import os
from common import save_result,read_json


domain='jd.com'


outfile='{0}.log'.format(domain)
# script_path=os.getcwd() #E:\SubDomain

script_path=os.path.dirname(os.path.abspath(__file__))
# print script_path
#
_cache_path = os.path.join(script_path,'result\{0}'.format(domain))
# print _cache_path
if not os.path.exists(_cache_path):
    os.makedirs(_cache_path,0777)


result = Crt(domain=domain).run()
_cache_file = os.path.join(_cache_path,'crt.json')
save_result(_cache_file, result)
# print result
#
result = Ilink(domain=domain).run()
_cache_file = os.path.join(_cache_path,'ilink.json')
save_result(_cache_file, result)
# print result


result = BaiduSite(domain=domain,pages=10).run()
_cache_file = os.path.join(_cache_path,'BaiduSite.json')
save_result(_cache_file, result)

# result = BruteDns(domain=domain).run()
# _cache_file = os.path.join(_cache_path,'BurteDns.json')
# save_result(_cache_file, result)
# # print result

result = BaiduSite(domain=domain,pages=10).run()
_cache_file = os.path.join(_cache_path,'Bing.json')
save_result(_cache_file, result)

_cache_files = ['crt.json','ilink.json','BaiduSite.json','Bing.json']

subdomains=[]

for file in _cache_files:
    _cache_file=os.path.join(_cache_path, file)
    json_data=read_json(_cache_file)
    if json_data:
        subdomains.extend(json_data)


subdomains = list(set(subdomains))

# print subdomains

result_file=os.path.join(script_path,outfile)
save_result(result_file,subdomains)

print '{0} {1} subdomains save to {2}'.format(domain,len(subdomains),result_file)
