# -*- coding: utf-8 -*-
'''
Created on 2016年1月31日

@author: Charlie
'''
from scrapy.spider import Spider
from scrapy.selector import Selector

#from dirbot.items import Article

import json
import re
import string
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

resp = HtmlResponse(url='http://bj.lianjia.com/ershoufang/dongcheng/pg1/')
print(resp)
#sel =Selector(response=resp).xpath('//*[@id="house-lst"]/li[1]/text()').extract()
sel =Selector(response=resp).xpath('/html/body/script[1]/text()').extract()

print(sel)

class SpiderTest(Spider):
  name = "SpiderTest"
  allowed_domains = ["lianjia.com"]
  
  start_urls = [
    'http://bj.lianjia.com/ershoufang/dongcheng/pg1/',
  ]
    
  def load_item(self, d):
    item = []
    title = d.xpath('header/h1/a')
    item['title'] = title.xpath('text()').extract()
    print item['title'][0]
    item['url'] = title.xpath('@href').extract()
    return item

  def parse_item(self, response):
    item = response.meta['item']
    
    sel = Selector(response)
    d = sel.xpath('//div[@class="entry-content"]/div')
    item['content'] = d.xpath('text()').extract()
    return item

  def parse(self, response):
    """
    The lines below is a spider contract. For more info see:
    http://doc.scrapy.org/en/latest/topics/contracts.html

    @url http://youyousuiyue.sinaapp.com
    @scrapes name
    """
    
    print 'parsing ', response.url
    sel = Selector(response)
    articles = sel.xpath('//div[@id="content"]/article')
    for d in articles:
      item = self.load_item(d)
      yield Request(item['url'][0], meta={'item':item}, callback=self.parse_item) # ** or yield item

    sel = Selector(response)
    link = sel.xpath('//div[@class="nav-previous"]/a/@href').extract()[0]
    if link[-1] == '4':
      return
    else:
      print 'yielding ', link
      yield Request(link, callback=self.parse)