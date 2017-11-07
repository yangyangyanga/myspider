# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class GpPipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, db='test',
                                    user='root', passwd='yangyaxia', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert into gupiao values('%s', '%s', '%s', '%s', '%s', '%s', " \
              "'%s', '%s', '%s', '%s', '%s')" % (
                item['xuhao'],item['jysj'],item['rz_ye'],item['rz_mre'],item['rz_che'],
                item['rz_rzjmr'],item['rq_yl'],item['rq_mcl'], item['rq_chl'],
                item['rq_rzjmq'],item['rq_rzrqye'] )
        self.cursor.execute(sql)
        return item

    def close_spider(self, spider):
        self.cursor.execute('commit')
        self.cursor.close()
        self.conn.close()

class IfengPipeline(object):
    def __init__(self):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, db='test',
                                    user='root', passwd='yangyaxia',charset='utf8')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        sql = "insert into ifeng values('%s', '%s')" % (item['title'], item['content'])
        self.cursor.execute(sql)
        return item

    def close_spider(self, spider):
        self.cursor.execute('commit')
        self.cursor.close()
        self.conn.close()