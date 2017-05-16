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


class NyaaMirrorResource(scrapy.Item):
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


class RarbgResource(scrapy.Item):
    name = scrapy.Field()  # 名字
    link = scrapy.Field()  # 磁链
    add_time = scrapy.Field()  # 添加时间
    size = scrapy.Field()  # 大小
    imdb_id = scrapy.Field()  # imdb_id
    title = scrapy.Field()  # 标题
    category = scrapy.Field()  # 分类
    year = scrapy.Field()  # 年份


class NyaaResource(scrapy.Item):
    name = scrapy.Field()
    category = scrapy.Field()
    date = scrapy.Field()
    submitter = scrapy.Field()
    seeders = scrapy.Field()
    information = scrapy.Field()
    leechers = scrapy.Field()
    size = scrapy.Field()
    downloads = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
