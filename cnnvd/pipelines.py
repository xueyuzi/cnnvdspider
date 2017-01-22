# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
class CnnvdPipeline(object):
    def __init__(self):
        self.connection = pymysql.connect(host='',
                             port=3306,
                             user= '',
                             password='',
                             db='',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO vulnerability(CNNVD_id,CVE_id,vulnerability_name,vulnerability_type,vulnerability_source,vulnerability_detail,vulnerability_notice,threat_type,release_time,update_time)VALUE('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (''.join(item['CNNVD_id']),''.join(item['CVE_id']),''.join(item['vulnerability_name']),''.join(item['vulnerability_type']),''.join(item['vulnerability_source']),''.join(item['vulnerability_detail']),''.join(item['vulnerability_notice']),''.join(item['threat_type']),''.join(item['release_time']),''.join(item['update_time'])))
        # print(''.join(item['CNNVD_id']),''.join(item['CVE_id']),''.join(item['vulnerability_name']),''.join(item['vulnerability_type']),''.join(item['vulnerability_source']))
        # print(''.join(item['vulnerability_detail']),''.join(item['vulnerability_notice']),''.join(item['threat_type']),''.join(item['release_time']),''.join(item['update_time']))
        self.connection.commit()
        return item
