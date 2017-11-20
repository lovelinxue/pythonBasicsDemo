# coding=utf-8
# lovelinxue
# theFileFunction: 
# -*- coding: utf-8 -*-

import html_Download,html_Outputer,html_Parser,url_Manager

class spiderMain(object):

    #类的初始化函数
    def __init__(self):
        #url管理器
        self.urls = url_Manager.UrlManager()
        #下载器
        self.downloader = html_Download.htmlDownloader()
        #解析器
        self.parser = html_Parser.htmlParser()
        #输出器
        self.outputer = html_Outputer.htmlOutputer()

    #类的方法
    def craw(self,root_url):

        #将入口URL添加到URL管理器
        self.urls.add_new_url(root_url)

        #显示第几个URL
        count = 1

        #开始循环
        while self.urls.has_new_url():

           # 拿到要爬的URL
           new_url = self.urls.get_new_url()

           print 'num %d : %s' % (count,new_url)

           # 启动下载器下载数据
           html_cont = self.downloader.download(new_url)
           # 将下载的页面进行解析数据(2个参数，当前爬的URL和下载好的数据)
           new_urls, new_data = self.parser.parser(new_url, html_cont)
           # 将新的URL地址添加到URL列表中
           self.urls.add_new_urls(new_urls)
           # 收集下载好的数据
           self.outputer.collect_data(new_data)

           # 限制循环次数
           if count == 60:
               break
           count += 1

        #输出收集好的数据信息
        self.outputer.output_html()



if __name__=='__main__':
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = spiderMain()
    obj_spider.craw(root_url)







