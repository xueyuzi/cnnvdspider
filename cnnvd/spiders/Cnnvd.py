# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from cnnvd.items import CnnvdItem
class VulnerabilitySpider(CrawlSpider):
    name = "Cnnvd"
    allowed_domains = ["www.cnnvd.org.cn"]
    start_urls = ['http://www.cnnvd.org.cn/vulnerability/']
    rules =(
        Rule(LinkExtractor(allow=("show/cv_id/\d+$")),callback="parse_item"),
        Rule(LinkExtractor(allow=("\?&p=\d+$")),follow=True),
    )

    def parse_item(self, response):
        self.logger.info(response.url)
        item =  CnnvdItem()
        details = response.xpath("//table[@class='details']")
        item['CNNVD_id'] = details.xpath("tr[2]/td[2]/text()").extract()
        item['CVE_id'] = details.xpath("tr[8]/td[2]/a/text()").extract()
        item['level'] = details.xpath("tr[5]/td[2]/a/text()").extract()
        item['vulnerability_name'] = details.xpath("tr[1]/td[2]/text()").extract()
        item['vulnerability_type'] = details.xpath("tr[6]/td[2]/a/text()").extract()
        item['vulnerability_source'] = details.xpath("tr[9]/td[2]/text()").extract()
        item['vulnerability_detail'] = response.xpath("//table[@width='100%']/tr[2]/td/div/p[1]/text()").extract()
        item['vulnerability_notice'] = response.xpath("//table[@width='100%']/tr[3]/td/div/p[1]/text()").extract() + response.xpath("//table[@width='100%']/tr[3]/td/div/p[1]/a/text()").extract()
        item['threat_type'] = details.xpath("tr[7]/td[2]/a/text()").extract()
        reference_data = response.xpath("//table[@width='100%']/tr[4]/td/div/table/tr/td/p")
        item['reference_site'] = reference_data.xpath('string(.)').extract()
        item['release_time'] = details.xpath("tr[3]/td[2]/a/text()").extract()
        item['update_time'] = details.xpath("tr[4]/td[2]/a/text()").extract()
        return item
