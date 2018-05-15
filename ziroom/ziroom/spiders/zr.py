# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule,CrawlSpider
from ziroom.items import ZiroomItem
from scrapy_redis.spiders import RedisCrawlSpider
import re


class ZrSpider(RedisCrawlSpider):
    name = 'zr'
    redis_key = 'Zr:start_urls'
    allowed_domains = ['ziroom.com']
    # start_urls = ['http://gz.ziroom.com/z/nl/z3.html?']

    rules = (
        Rule(LinkExtractor(allow=(r'http://gz.ziroom.com/z/nl/z3.html?p=\d+'),
                           restrict_xpaths=('//*[@id="page"]/a[5]'))),
        Rule(LinkExtractor(allow=(r'http://gz.ziroom.com/z/vr/\d+.html')), callback='parse_item'),
    )

    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(ZrSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = ZiroomItem()
        item['name'] = response.xpath('/html/body/div[3]/div[2]/div[1]/h2/text()').extract()[0].strip()

        item['area'] = response.xpath('/html/body/div[3]/div[2]/ul/li[1]/text()').extract()[0].strip()[3:].replace('\n','').replace(' ','')
        item['face'] = response.xpath('/html/body/div[3]/div[2]/ul/li[2]/text()').extract()[0].strip()[3:].replace(' ','')
        item['house_ty'] = response.xpath('/html/body/div[3]/div[2]/ul/li[3]/text()').extract()[0].strip()[3:].replace(
            ' ', '')
        item['floor'] = response.xpath('/html/body/div[3]/div[2]/ul/li[4]/text()').extract()[0].strip()[3:].replace(' ',
                                                                                                                    '')
        item['price'] = response.xpath('//*[@id="room_price"]/text()').extract()[0].strip()[1:] + '元'
        return item