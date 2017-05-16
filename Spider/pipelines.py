# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import re


class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class NyaaMirrorSpiderPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('nyaa_mirror.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS sukebei_pantsu_cat(
          hash TEXT PRIMARY KEY NOT NULL ,
          name TEXT NOT NULL ,
          link TEXT NOT NULL 
        )''')

    def process_item(self, item, spider):
        if spider.name != 'nyaa_mirror':
            return item
        sql = '''INSERT OR IGNORE INTO sukebei_pantsu_cat(name, hash, link) VALUES (?,?,?)'''
        self.conn.execute(sql, (item['name'], item['hash'], item['link']))
        self.conn.commit()

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
        if spider.name != 'dmhy':
            return item
        sql = '''INSERT OR IGNORE INTO share_dmhy_org(name,size,release_time,modify_time,magnet1,magnet2,info,classify) VALUES (?,?,?,?,?,?,?,?)'''
        self.conn.execute(sql, (
            item['name'], item['size'], item['release_time'], item['modify_time'], item['magnet1'], item['magnet2'],
            item['info'], item['classify']))
        self.conn.commit()

    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None


class RarbgSpiderPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('rarbg.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS rarbg_to(
            name TEXT,
            link TEXT,
            add_time TEXT,
            size TEXT,
            imdb_id TEXT,
            title TEXT,
            category TEXT,
            year TEXT
        )''')

    def process_item(self, item, spider):
        if spider.name != 'rarbg':
            return item
        if item['imdb_id']:
            item['imdb_id'] = re.match(".*/(.*)/", item['imdb_id']).group(1)
        sql = '''INSERT INTO rarbg_to (name, link, add_time, size, imdb_id, title, category, year) VALUES (?,?,?,?,?,?,?,?)'''
        self.conn.execute(sql, (
            item['name'],
            item['link'],
            item['add_time'],
            item['size'],
            item['imdb_id'],
            item['title'],
            item['category'],
            item['year']
        ))
        self.conn.commit()

    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None


class NyaaSpiderPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('nyaa.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS nyaa(
            name TEXT,
            category TEXT,
            date TEXT,
            submitter TEXT,
            seeders TEXT,
            information TEXT,
            leechers TEXT,
            size TEXT,
            downloads TEXT,
            link TEXT,
            description TEXT
        )''')

    def process_item(self, item, spider):
        if spider.name != 'nyaa':
            return item
        sql = '''INSERT INTO nyaa(name,category,date,submitter,seeders,information,leechers,size,downloads,link,description)
                  VALUES (?,?,?,?,?,?,?,?,?,?,?)'''
        self.conn.execute(sql, (
            item['name'],
            item['category'],
            item['date'],
            item['submitter'],
            item['seeders'],
            item['information'],
            item['leechers'],
            item['size'],
            item['downloads'],
            item['link'],
            item['description']
        ))
        self.conn.commit()

    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None
