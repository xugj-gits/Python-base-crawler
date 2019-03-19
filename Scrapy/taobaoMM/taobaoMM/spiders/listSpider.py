# -*- coding: utf-8 -*-
import scrapy
import os


class ListspiderSpider(scrapy.Spider):
    name = 'listSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        sayings = response.css('div.quote')

        for saying in sayings:
            text = saying.css('.text::text').extract_first()
            autor = saying.css('.author::text').extract_first()
            tags = saying.css('.tags .tag::text').extract()
            tags = ','.join(tags)

            filename = '%s-语录.txt' % autor

            with open(filename, 'a+') as f:
                if os.path.getsize(filename):
                    f.write('\n')
                f.write(text)
                f.write('\n')
                f.write('标签:' + tags)
                f.write('\n' + '-'*20)
                f.close()
