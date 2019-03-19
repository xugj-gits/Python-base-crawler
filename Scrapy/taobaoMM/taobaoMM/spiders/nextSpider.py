# -*- coding: utf-8 -*-
import scrapy
import os


class NextspiderSpider(scrapy.Spider):
    name = 'nextSpider'
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

        next_page = response.css('li.next a::attr(href)').extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
