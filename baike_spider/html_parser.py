#coding:utf-8
import urlparse
from bs4 import BeautifulSoup
import re

__author__ = 'Administrator'


class HtmlParser (object):
    def parse (self , url , html_cont):
        """
        解析函数：
        用来解析下载好的网页，最后会得到解析页面上的各个新链接和内容
        主要通过两个函数实现
        For parse the downloaded web page, in the end we will get every new link and data we need in this page.
         mainly  enable the function by two self methods (_get_new_urls , _get_new_data)
        :param url:
        :param html_cont:
        :return:
        """
        if url is None or html_cont is None :
            return

        soup = BeautifulSoup(html_cont , 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(url , soup)
        new_data = self._get_new_data(url , soup)
        return  new_urls , new_data

    def _get_new_urls (self , url , soup):
        """
        实现得到当前网页上的新链接的功能。
        actualize the function that is to get new links in current page.
        :param url:
        :param soup:
        :return:
        """
        #href="/view/147669.htm"
        new_urls = set()
        links = soup.find_all('a', href = re.compile(r"/view/\d+\.htm")) #匹配正则表达式r"/view/\d+\.htm"
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url , new_url)
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data (self , url , soup):
        """
        实现得到当前网页上的摘要内容和标题的功能。
        actualize the function that is to get titles and summary in current page.

        :param url:
        :param soup:
        :return:
        """
        rest_data ={}
        #url
        rest_data['url'] = url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1> 标题的html格式
        title_node = soup.find('dd', class_ ="lemmaWgt-lemmaTitle-title" ).find('h1')
        rest_data['title'] =  title_node.get_text()
        #<div class="lemma-summary" label-module="lemmaSummary"> 摘要的html格式
        summary_node = soup.find('div' , class_ = "lemma-summary")
        rest_data['summary'] = summary_node.get_text()

        return rest_data

