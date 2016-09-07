#coding:utf-8
__author__ = 'Administrator'


class UrlManager (object):
    def __init__(self):
        """
        创建两个集合，一个是存储新的url，一个存储已爬取过的url
        create two sets , one save totally new page url; the other save the url which has been crawled
        :return:
        """
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url (self , url):
        """
        添加新的url进new_urls集合
        add one new url into new_urls set
        :param url:
        :return:
        """
        if url is None:
            return
        if url  not in self.new_urls and url  not  in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls (self , urls):
        """
        添加从网页内容解析出来的新urls
        add new urls which are parsed from the page content
        :param urls:
        :return:
        """
        if urls is None or len(urls) == 0 :
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url (self):
        """
        判断是否有未爬取的新url
        determine whether the new  url  which has not been crawled exist in new_urls set
        :return:
        """
        return len(self.new_urls) != 0

    def get_new_url (self):
        """
        获取一个新的url进行操作
        get one new url  to the next procedure
        :return:
        """
        new_url= self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

