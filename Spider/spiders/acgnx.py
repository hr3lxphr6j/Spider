# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class AcgnxSpider(scrapy.Spider):
    name = "acgnx"
    allowed_domains = ["acgnx.se"]
    start_urls = ['https://www.acgnx.se/']

    def parse(self, response):
        nodes = response.css("#listTable tbody tr")
        pass
