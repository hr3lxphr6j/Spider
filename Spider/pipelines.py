# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class NyaaSpiderPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('nyaa.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS sukebei_pantsu_cat(
          hash TEXT PRIMARY KEY NOT NULL ,
          name TEXT NOT NULL ,
          link TEXT NOT NULL 
        )''')

    def process_item(self, item, spider):
        if spider.name == 'nyaa':
            sql = '''INSERT OR IGNORE INTO sukebei_pantsu_cat(name, hash, link) VALUES (?,?,?)'''
            self.conn.execute(sql, (item['name'], item['hash'], item['link']))
            self.conn.commit()
        else:
            return item

    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None


class DmhySpiderPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('dmhy.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS share_dmhy_org(
            name TEXT,
            size TEXT,
            release_time TEXT,
            modify_time TEXT,
            magnet1 TEXT,
            magnet2 TEXT,
            info TEXT,
            classify TEXT
        )''')

    def process_item(self, item, spider):
        if spider.name == 'dmhy':
            sql = '''INSERT OR IGNORE INTO share_dmhy_org(name,size,release_time,modify_time,magnet1,magnet2,info,classify) VALUES (?,?,?,?,?,?,?,?)'''
            self.conn.execute(sql, (
                item['name'], item['size'], item['release_time'], item['modify_time'], item['magnet1'], item['magnet2'],
                item['info'], item['classify']))
            self.conn.commit()
        else:
            return item

    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None
