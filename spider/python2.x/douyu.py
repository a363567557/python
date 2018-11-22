#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import signal
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0


class douyu(unittest.TestCase):
    #初始化方法，必须是setup()
    def setUp(self):
	#executable_path = "/usr/bin/phantomjs"
        self.driver = webdriver.Chrome()
        self.num = 0
        self.count = 0
	self.page = 0

    #测试方法必须有test字样开头
    def testDouyu(self):
	print "*********"
        self.driver.get("https://www.douyu.com/directory/all")
       	while True:
	    print "######"
	    soup = bs(self.driver.page_source, "lxml")
	    #房间名，返回列表
	    names = soup.find_all("h3",{"class":"ellipsis"})
	    #观众人数，返回列表
	    numbers = soup.find_all("span",{"class":"dy-num fr"})
	    
	    #zip(names,numbers) 将name和number两个列表合并成为一个元组
	    for name,number in zip(names,numbers):
		print u"观众人数：--"+number.get_text().strip() + u"-\t房间名字： "+number.get_text().strip()
		self.num+=1

	    time.sleep(5)
	     # 点击前往下一页
	    if self.driver.page_source.find("shark-pager-disable-next") != -1:
	    	print("-------")
		break
	    

	    #一直点击下一页
	    if self.driver.page_source.find("shark-pager-next") != -1:
		self.driver.find_element_by_class_name("shark-pager-next").click()
	    	self.page = self.page + 1
	    	print self.page
	    


    #测试结束执行的方法
    def testDown(self):
	print "测试结束执行的方法"
        #退出PhantomJS()浏览器
        print "当前网站直播人数："+str(self.num)
        # print "当前网站观众人数："+str(self.count)
        self.driver.quit()

if __name__ == "__main__":
    #启动测试模块
    print "启动测试模块"
    unittest.main()

