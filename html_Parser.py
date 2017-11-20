# coding=utf-8
# lovelinxue
# theFileFunction: 
# -*- coding: utf-8 -*-
import re
import urlparse
from bs4 import BeautifulSoup


class htmlParser(object):

    def parser(self, new_url, html_cont):

        if new_url is None or html_cont is None:
            print 'parser 中的参数有空为空'
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')

        newUrlList = self.getNewUrlListAction(new_url,soup)
        newDataList = self.getNewDataListAction(new_url,soup)

        return newUrlList,newDataList

    def getNewUrlListAction(self, page_url, soup):
        newUrlList = set()

        links = soup.find_all('a',href=re.compile(r'/item/'))

        for link in links:
            newUrl = link['href']
            newFullUrl = urlparse.urljoin(page_url,newUrl)
            newUrlList.add(newFullUrl)

        return newUrlList


    def getNewDataListAction(self, page_url, soup):

        newDict = {}

        #保存url地址
        newDict['url'] = page_url

        #根据网页结构拉取标题数据
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        titleStr = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        newDict['title'] = titleStr.get_text()

        #根据网页结构拉取简介
        #<div class="lemma-summary" label-module="lemmaSummary">
        contentStr = soup.find('div',class_='lemma-summary')

        if contentStr is not None:
            newDict['content'] = contentStr.get_text()
        else:
            subStr = soup.find('div',class_='lemmaWgt-subLemmaListTitle')
            if subStr is not None:
                newDict['content'] = subStr.get_text()

        return newDict