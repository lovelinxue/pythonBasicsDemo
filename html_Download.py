# lovelinxue
# theFileFunction: 
# -*- coding: utf-8 -*-
import urllib2


class htmlDownloader(object):

    def download(self, url):

        if url is None:
            return None

        respones = urllib2.urlopen(url)

        if respones.getcode() != 200:
            return None

        return respones.read()

