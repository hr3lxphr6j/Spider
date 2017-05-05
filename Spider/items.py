# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NyaaResource(scrapy.Item):
    name = scrapy.Field()  # 名字
    hash = scrapy.Field()  # 哈希
    link = scrapy.Field()  # 磁链


class DmhyResource(scrapy.Item):
    name = scrapy.Field()  # 名字
    size = scrapy.Field()  # 文件大小
    release_time = scrapy.Field()  # 發佈時間
    modify_time = scrapy.Field()  # 修改時間
    magnet1 = scrapy.Field()  # 磁链Type1
    magnet2 = scrapy.Field()  # 磁链Type2
    info = scrapy.Field()  # 发布信息
    classify = scrapy.Field()  # 分类
    pass
