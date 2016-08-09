# coding:utf-8
from baike_spider import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self) :              
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()
	
	def craw(self,root_url,num):                  
	    count = 1
	    self.urls.add_new_url(root_url)        # url管理器加入根链接
	    while(self.urls.has_new_url()):        # 当管理器中存在链接
			try:
				new_url = self.urls.get_new_url()         #url管理器 取出一个url
				print  'craw %d : %s ' % (count, new_url)
				html_content = self.downloader.download(new_url)        # 下载器通过url下载一个网页文档
				new_urls, new_data = self.parser.parse(new_url, html_content)    # 解析器通过文档解析出新文档与需要的数据
				self.urls.add_new_urls(new_urls)      
	            self.outputer.collect_data(new_data)  # 输出器收集数
			except:
				print 'craw failed'                #当前页面爬取失败

			count = count + 1
			if count > num :
				break
		self.outputer.output_html()    

if __name__=="__main__":
    root_url="http://baike.baidu.com/link?url=DwQd6j2iC_BOdWhM645mbHcxgKFerheCISzWHbHZfyuzDiq2kfdlFHkRKjGzp9N2YznXdIw6TMCprdA-BhuaFq"   
	num=100
    obj_spider=SpiderMain()
    obj_spider.craw(root_url,num)
