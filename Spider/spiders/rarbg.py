# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from scrapy.http import Request
import re
from Spider.items import RarbgResource


HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/60.0.3091.0 Safari/537.36 "
}
COOKIES = {
    "abu": "1",
    "q2bquVJn": "qCBnZk87",
    "skt": "swgv4xa2fq",
    "LastVisit": "1494237597"
}


class RarbgSpider(scrapy.Spider):
    name = "rarbg"
    allowed_domains = ["rarbg.to"]
    start_urls = ['https://rarbg.to/torrents.php']

    def start_requests(self):
        return [Request(
            url=self.start_urls[0],
            headers=HEADER,
            cookies=COOKIES
        )]

    def parse(self, response):
        self.set_last_view(response)
        nodes = response.css(".lista2t tr")
        for node in nodes[1:]:
            detail_url = node.css("a[onmouseover]::attr(href)").extract_first("")
            yield Request(
                url=parse.urljoin(response.url, detail_url),
                headers=HEADER,
                cookies=COOKIES,
                callback=self.parse_detail
            )
        next_url = response.css('a[title*="next page"]::attr(href)').extract_first("")
        yield Request(
            url=parse.urljoin(response.url, next_url),
            headers=HEADER,
            cookies=COOKIES,
            callback=self.parse
        )
        pass

    def parse_detail(self, response):
        self.set_last_view(response)
        resource = RarbgResource()
        table = response.css('table[class="lista"] table[width="100%"]')
        resource['name'] = response.css('h1[itemprop="name"]::text').extract_first("")
        resource['link'] = table.css('tr').css('td')[1].css('a')[1].css("::attr(href)").extract_first("")
        resource['add_time'] = self.parse_table(table, "Added")
        resource['size'] = self.parse_table(table, "Size")
        resource['imdb_id'] = table.css('img[src*="imdb"]').xpath("../following-sibling::*[1]").css(
            "::text").extract_first("")
        resource['title'] = self.parse_table(table, "Title")
        resource['category'] = self.parse_table(table, "Category")
        resource['year'] = self.parse_table(table, "Year")
        yield resource

    def parse_table(self, table, name):
        try:
            return table.xpath("//td[contains(.//text(), '%s:')]/following-sibling::*[1]" % name).css(
                "::text").extract_first("")
        except IndexError:
            return ""

    @staticmethod
    def set_last_view(response):
        if response.headers.getlist('Set-Cookie'):
            m = re.match(".*LastVisit=(.*);.*", response.headers.getlist('Set-Cookie')[0].decode("utf-8"))
            if m:
                COOKIES['LastVisit'] = m.group(1)
