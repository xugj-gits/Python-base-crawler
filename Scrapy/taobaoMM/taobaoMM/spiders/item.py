#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   item.py
@Time    :   2019/03/14 17:03:04
@Author  :   高效码农 
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''
import scrapy


class ItemSpider(scrapy.Spider):
    name = 'item'
    allowed_domains = ['http://lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        saying = response.css('div.quote')[0]

        text = saying.css('.text::text').extract_first()
        autor = saying.css('.author::text').extract_first()
        tags = saying.css('.tags .tag::text').extract()
        tags = ','.join(tags)

        fileName = '%s-语录.txt' % autor
        with open(fileName, 'a+') as f:
            f.write(text)
            f.write('\n')

        self.log('保存文件：%s' % fileName)
