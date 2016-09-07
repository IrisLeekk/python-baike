#coding:utf-8
from baike_spider import url_manager,html_downloader,html_parser,html_outputer

__author__ = 'Administrator'


class SpiderMain (object):
    def __init__(self):
        """构造函数
        声明各个模块函数
        urls为url管理器
        downloader为网页下载器
        parser为网页解析器
        outputer为网页输出
        """
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()



    def crawl(self, root_url):
        """
        main function主要功能
        crawl  web pages 爬取网页
        download 1000 pages in root web page, then parse their contents and print the analysed data in the screen
        在新网页中把网页内容进行下载到本地，然后进行解析输出。爬取1000次。
        :param root_url:
        :return:
        """
        count = 1
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "%d %s" %(count , new_url)
                html_cont = self.downloader.download(new_url)
                new_urls , new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 10:
                     break
                count = count + 1
            except:
                print "crawl failed !"

        self.outputer.output_html()
#主函数main method
#根页面为python的百度词条 root url is the baike web page about python
if __name__ == '__main__':
    root_url = "http://baike.baidu.com/link?url=rq_mSHH1MHV21_EAWrE1vbwDcPYGjv_9Z3aoMYpfiplcQ9c8ky6sH5Loneneg2lDOAUdcRXWwiielPj5nQ7lAq"
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)
    
