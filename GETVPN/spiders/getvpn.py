# -*- coding: utf-8 -*-
import scrapy

from GETVPN.items import GetvpnItem

class GetvpnSpider(scrapy.Spider):
    name = "getvpn"
    allowed_domains = ["vpngate.com"]
    start_urls = ['http://www.vpngate.net/cn/']

    def parse(self, response):
        items = []
        for href in response.xpath("//td//@href").extract():
            if str(href).startswith('do_openvpn'):
                items.append(href)
        yield items
