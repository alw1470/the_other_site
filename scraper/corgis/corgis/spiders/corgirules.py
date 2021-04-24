# -*- coding: utf-8 -*-
import scrapy


class CorgirulesSpider(scrapy.Spider):
    name = 'corgirules'
    allowed_domains = ['gettyimages.es']
    start_urls = ['https://www.gettyimages.es/fotos/pembroke-welsh-corgi?sort=best&mediatype=photography&phrase=pembroke%20welsh%20corgi']

    def parse(self, response):             
        imagenes = response.xpath('//figure[@class="gallery-mosaic-asset__figure"]//@src').extract()
        for imagen in imagenes:
            yield{'imagen':imagen}
        pass
