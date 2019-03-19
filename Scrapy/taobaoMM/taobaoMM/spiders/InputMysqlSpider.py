#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   scrapyMysql.py
@Time    :   2019/03/15 10:17:43
@Author  :   高效码农 
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''

import scrapy
from taobaoMM.items import TaobaommItem


class InputMysqlSpider(scrapy.Spider):
    name = 'inputMysql'
    allowed_domains = ["lab.scrapyd.cn"]
    start_urls = ['http://lab.scrapyd.cn/']


    def parse(self, response):
        sayings = response.css('div.quote')

        item = TaobaommItem()
        for saying in sayings:
            item['cont'] = saying.css('.text::text').extract_first()

            tags = saying.css('.tags .tag::text').extract()
            item['tag'] = ','.join(tags)

            item['autor'] = saying.css('.author::text').extract_first()

            yield item

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)  # 提交给parse继续抓取下一页
