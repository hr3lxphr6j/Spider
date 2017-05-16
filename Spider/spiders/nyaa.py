# -*- coding: utf-8 -*-
import scrapy
import cfscrape
from urllib import parse
from scrapy.http import Request
from Spider.items import NyaaResource


class NyaaSpider(scrapy.Spider):
    name = "nyaa"
    allowed_domains = ["nyaa.si"]
    start_urls = ['https://nyaa.si/,https://sukebei.nyaa.si/']
    HEADERS, COOKIES = {}, {}

    def start_requests(self):
        if not self.HEADERS or not self.COOKIES:
            self.COOKIES, self.HEADERS['User-Agent'] = cfscrape.get_tokens(self.start_urls[0])
        return [Request(
            url=self.start_urls[0],
            headers=self.HEADERS,
            cookies=self.COOKIES
        )]

    def parse(self, response):
        nodes = response.css("table tbody tr")
        for node in nodes:
            detail_url = node.css("td a::attr(href)")[1].extract()
            yield Request(
                url=parse.urljoin(response.url, detail_url),
                headers=self.HEADERS,
                cookies=self.COOKIES,
                callback=self.parse_detail
            )
        next_url = response.css(".pagination li a::attr(href)")[-1].extract()
        yield Request(
            url=parse.urljoin(response.url, next_url),
            headers=self.HEADERS,
            cookies=self.COOKIES
        )
        pass

    def parse_detail(self, response):
        info_name = ['category', 'date', 'submitter', 'seeders',
                     'information', 'leechers', 'size', 'downloads']
        resource = NyaaResource()
        resource['name'] = response.css('h3[class="panel-title"]::text').extract()[0].replace('\n', '')
        resource['link'] = response.css('a[href*="magnet:?"]::attr(href)').extract_first("")
        resource['description'] = response.css('#torrent-description').extract_first("")
        info_list = response.css('.panel-body .row .col-md-5')
        for info, name in zip(info_list, info_name):
            resource[name] = ''.join(info.css('::text').extract()).replace('\n', '')
        yield resource
