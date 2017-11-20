# coding=utf-8
# lovelinxue
# theFileFunction: 
# -*- coding: utf-8 -*-

class UrlManager(object):

    #初始化类函数
    def __init__(self):
        self.new_urlArray = set()
        self.old_urlArray = set()

    #向管理器中添加一个url
    def add_new_url(self, url):
        #如果url为空，返回
        if url is None:
            print 'url_Manager_add_new_url 为空'
            return

        #如果url没有在待爬取和已爬取列表
        if url not in self.new_urlArray and url not in self.old_urlArray:
            self.new_urlArray.add(url)

    # 向管理器中添加多个url
    def add_new_urls(self, urls):
        #判断是否为空
        if urls is None or len(urls) == 0:
            print 'add_new_urls函数为空'
            return

        for url in urls:
            self.add_new_url(url)


    # 判断管理器中是否有新的待爬取的url
    def has_new_url(self):
        return len(self.new_urlArray) != 0


    # 从管理器中读取一个url
    def get_new_url(self):
        new_url = self.new_urlArray.pop()
        self.old_urlArray.add(new_url)
        return new_url

