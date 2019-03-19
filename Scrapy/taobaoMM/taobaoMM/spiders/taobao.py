#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   taobao.py
@Time    :   2019/03/14 15:36:26
@Author  :   高效码农
@Version :   1.0
@Contact :   514583562@qq.com
@License :   (C)Copyright 2019-2020, xugj520.cn
@Desc    :   None
'''

import scrapy


class taobaoMM(scrapy.Spider):

    name = "taobaoMM"

    def start_requests(self):

        urls = [
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'taobaoMM-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件：%s' % filename)
