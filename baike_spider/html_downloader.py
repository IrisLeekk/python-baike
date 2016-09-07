#coding:utf-8
import urllib2

__author__ = 'Administrator'


class HtmlDownloader (object):


    def download (self , url):
        """
        下载url内容数据到本机
        download url content data to local
        :param url:
        :return:
        """
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:   #网络状态码http Status-Code 200 是正常网络连接
            return None

        return response.read()



