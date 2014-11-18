#coding=utf-8

from scrapy.spider import Spider
from scrapy.selector import Selector

#第一个DmozItem是模块名(文件名,命名空间),第二个是类名
#from tutorial.DmozItem  import DmozItem

#这里items是模块名(文件名，命名空间),DmozItem是类名
from tutorial.items  import DmozItem

##copy
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
import sys
import string
sys.stdout=open('output_cnds.txt','w') #将打印信息输出在相应的位置下

class DmozSpider(Spider):
    name = "dmoz"
    #allowed_domains = ["dmoz.org"]
    allowed_domains = []
    start_urls = [
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        #"http://www.dmoz.org/"
		"http://blog.csdn.net/blogdevteam"
    ]

    def parse(self, response):
#        filename = response.url.split("/")[-2]
#        open(filename, 'wb').write(response.body)
		sel = Selector(response)
		#sites = sel.xpath('//ul[@class="directory-url"]/li')
		sites = sel.xpath('//ul/li')
		#sites = sel.xpath('//ul/li')
		items = []
		for site in sites:
			#title = site.xpath('a/text()').extract()
			#link = site.xpath('a/@href').extract()
			#desc = site.xpath('text()').extract()
			#print title
			#print title,link,desc
			item = DmozItem();
			item['title'] = site.xpath('a/text()').extract()
			item['link'] = site.xpath('a/@href').extract()
			item['desc'] = site.xpath('text()').extract()
			items.append(item)

			for  j in item['title']:
				print '标题:',j.encode('utf-8')
			for  j in item['link']:
				print '链接:',j.encode('utf-8')
			for  j in item['desc']:
				print '正文:',j.encode('utf-8')
		sys.stdout.close()#=open('output_cnds.txt','w') #将打印信息输出在相应的位置下
		#return  0 
		return  items

