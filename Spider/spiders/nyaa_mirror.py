# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from Spider.items import NyaaResource


class NyaaMirrorSpider(scrapy.Spider):
    name = "nyaa_mirror"
    allowed_domains = ["sukebei.pantsu.cat"]
    start_urls = ['https://sukebei.pantsu.cat/']

    def parse(self, response):
        for i in range(10727, 33737):  # 10727 33737
            yield Request(url='https://sukebei.pantsu.cat/page/' + str(i),
                          callback=self.parse_resource)
        pass

    def parse_resource(self, response):
        rows = response.xpath("//tr")
        for row in rows[1:]:
            resource = NyaaResource()
            resource['name'] = row.xpath("./td[1]/text()").extract_first('')
            resource['hash'] = row.xpath("./td[2]/text()").extract_first('')
            resource['link'] = row.xpath("./td[3]/a[1]/@href").extract_first('')
            yield resource
        pass
