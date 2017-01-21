# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnnvdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    CNNVD_id = scrapy.Field()
    CVE_id = scrapy.Field()
    level = scrapy.Field()
    vulnerability_name = scrapy.Field()
    vulnerability_type = scrapy.Field()
    vulnerability_source = scrapy.Field()
    vulnerability_detail = scrapy.Field()
    vulnerability_notice = scrapy.Field()
    threat_type = scrapy.Field()
    reference_site = scrapy.Field()
    release_time = scrapy.Field()
    update_time = scrapy.Field()
