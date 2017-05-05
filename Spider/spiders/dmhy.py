# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from Spider.items import DmhyResource


class DmhySpider(scrapy.Spider):
    name = "dmhy"
    allowed_domains = ["share.dmhy.org"]
    start_urls = ['https://share.dmhy.org/topics/list/page/1']

    def parse(self, response):
        nodes = response.css(".tablesorter tbody tr")
        for node in nodes:
            detail_url = node.css(".title a::attr(href)").extract()[-1]
            yield Request(parse.urljoin(response.url, detail_url), callback=self.parse_detail)
        next_url = response.xpath("/html/body/div/div/div[2]/div[8]/div[1]/div[1]/a[last()]/@href").extract_first("")
        yield Request(parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        resource = DmhyResource()
        info = response.css(".resource-info ul li")
        resource['name'] = response.css(".topic-title h3::text").extract_first("")
        resource['size'] = info[-3].css("span::text").extract_first("")
        resource['release_time'] = info[1].css("span::text").extract_first("")
        resource['modify_time'] = info[2].css("span::text").extract_first("")
        resource['classify'] = info[0].css("span a")[-1].css("::text").extract_first("")
        resource['info'] = response.css(".topic-nfo").extract_first("")
        resource['magnet1'] = response.css("#a_magnet::attr(href)").extract_first("")
        resource['magnet2'] = response.css("#magnet2::attr(href)").extract_first("")
        yield resource
