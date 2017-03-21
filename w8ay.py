#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:w8ayScan
Author:w8ay
Copyright (c) 2017
'''
import sys
from lib.core.Spider import SpiderMain
from lib.core import webcms,PortScan,common,webdir,fun_until
from lib.core import outputer

reload(sys)
sys.setdefaultencoding('utf-8')
def main():
    root = "https://www.shiyanlou.com/"
    domain = common.w8urlparse(root)
    threadNum = 10
    output = outputer.outputer()
    # CDN Check
    print "CDN check...."
    iscdn = True
    try:
        msg,iscdn =  fun_until.checkCDN(root)
        output.add("cdn",msg)
        output.build_html(domain)
        print msg
    except:
        print "[Error]:CDN check error"

    if iscdn:
        #IP Ports Scan
        ip = common.gethostbyname(root)
        print "IP:",ip
        print "START Port Scan:"
        pp = PortScan.PortScan(ip)
        pp.work()
        output.build_html(domain)
    
    # DIR Fuzz
    dd = webdir.webdir(root,threadNum)    
    dd.work()
    dd.output()
    output.build_html(domain)
    #webcms
    ww = webcms.webcms(root,threadNum)
    ww.run()
    output.build_html(domain)
    #spider
    w8 = SpiderMain(root,threadNum)
    w8.craw()

if __name__ == '__main__':
    main()