#!/usr/bin/env python
# -*-coding:utf-8 -*-

import dns.resolver
import sys
import threading
from Queue import Queue
from config import *

class BruteDns(object):
    def __init__(self,domain):
        self.domain = domain
        self.thread_count = thread_count
        self.queue = Queue()
        self.result = []

    def run(self):
        #调用多线程方式进行暴力破解
        with open('dict/subname.txt') as f:
            for i in f:
                i = i.replace('\n','').strip()
                # print i
                self.queue.put(i + '.' + self.domain)

            threads=[]
            total = self.queue.qsize()
            # print total

            for i in xrange(self.thread_count):
                threads.append(self.BruteRun(self.queue,self.result,total))
            for i in threads:
                i.start()
            for i in threads:
                i.join()
            return list(set(self.result))



    class BruteRun(threading.Thread):
        def __init__(self,queue,result,total):
            threading.Thread.__init__(self)
            self._queue = queue
            self._result = result
            self._total=total

        def run(self):
            while not self._queue.empty():
                sub = self._queue.get()
                # print '[*trying] '+sub
                try:
                    result = dns.resolver.query(sub,'A')
                    # print result
                    if result.response.answer:
                        # self.message()
                        # print '[Success] '+sub
                        self._result.append(sub)
                        self.message()
                        # print len(self._result)
                except Exception,e:
                    pass

        def message(self):
            DoneCount=self._total - self._queue.qsize()
            AllCount = self._total
            FoundCount=len(self._result)
            # print AllCount
            message = '[-]Total {} [-]Done {} [-]Found {}'.format(AllCount,DoneCount,FoundCount)
            sys.stdout.write('\r'+message)
            sys.stdout.flush()