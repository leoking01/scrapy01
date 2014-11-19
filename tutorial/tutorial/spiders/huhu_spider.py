# -*- coding:utf-8 -*-
# -*- coding:gbk2312 -*-
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
#from dirbot.items import Website
#from tutorial.items import Website
from tutorial.items import Website
import sys
import string
sys.stdout=open('output_huhu.txt','w') #将打印信息输出在相应的位置下
print '----------output_huhu.txt  has been opend.-----------------'

add = 0
class DmozSpider(CrawlSpider):

    name = "huhu"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "http://www.cnblogs.com/huhuuu",
    ]

    
	#print 'huhu--b'
    rules = (
        # 提取匹配 huhuuu/default.html\?page\=([\w]+) 的链接并跟进链接(没有callback意味着follow默认为True)
        Rule(SgmlLinkExtractor(allow=('huhuuu/default.html\?page\=([\w]+)', ),)),

        # 提取匹配 'huhuuu/p/' 的链接并使用spider的parse_item方法进行分析
        Rule(SgmlLinkExtractor(allow=('huhuuu/p/', )), callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=('huhuuu/archive/', )), callback='parse_item'), #以前的一些博客是archive形式的所以
    )

    def parse_item(self, response):
        print '----------------huhu--c---start-------'
        global add #用于统计博文的数量
        
        print  add
        add+=1
        
        sel = Selector(response)
        items = []

        item = Website()
        item['headTitle'] = sel.xpath('/html/head/title/text()').extract()#观察网页对应得html源码
        item['url'] = response
        #print item  
		## my mify following


        print 'type(item)=',type(item)
        print "type(item['url'])=",type(item['url'])
        #print item['headTitle'].encode('utf-8')
        for ii in item['headTitle']:
            print ii.encode('utf-8')

        #    for jj in item['url']:
         #       print jj.encode('utf-8')

        items.append(item)
        return items
        sys.stdout.close()#=open('output_huhu.txt','w') #将打印信息输出在相应的位置下
        print '---------------output_huhu.txt  close-------------'
        
        ####my add
        quit()
