#coding:utf-8
from bs4 import BeautifulSoup                # html解析器模块
import re
import urlparse

class HtmlParser(object):

	    def get_new_urls(self, url, soup):
	        # <a target="_blank" href="/view/845405.htm">Unix shell</a>
			new_urls = set()
	        links = soup.find_all('a' , href = re.compile(r'/view/\d+.htm'))          #匹配相对ur
			for link in links:
				new_url = link['href']                       
				new_full_url = urlparse.urljoin(url,new_url)           #通过本url格式补全相对url
				new_urls.add(new_full_url)                           
	        return new_urls
			        
	    def get_new_datas(self, url, soup):
			new_dict = {}
			
			new_dict['url'] = url
			#  <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>			
			title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')          #找到标题节点
			new_dict['title'] = title_node.get_text()
			#<div class="lemma-summary" label-module="lemmaSummary">
			summary_node = soup.find('div', class_='lemma-summary')                       #找到简洁节点			
			new_dict['summary'] = summary_node.get_text()
																	        
	        return new_dict
										
		def parse(self, url ,content): 
			if url is None or content is None:
				return

			soup = BeautifulSoup(content,'html.parser',from_encoding='utf-8')     #通过html文件  解析该页面			
	        new_urls = self.get_new_urls(url,soup)
	        new_datas = self.get_new_datas(url,soup)
	        
	        return new_urls,new_datas
			    

