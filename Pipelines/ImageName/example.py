# -*- coding: utf-8 -*-
import pathlib
import scrapy
from scrapy.settings import Settings
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor

class DQItem(scrapy.Item):
    title = scrapy.Field()
    logo = scrapy.Field()
    logo_path = scrapy.Field()
    slime = scrapy.Field()
    slime_path = scrapy.Field()
    images = scrapy.Field()

class DQSpider(scrapy.Spider):
    name = 'dq'
    start_urls = ['https://en.wikipedia.org/wiki/Dragon_Quest']

    def parse(self, response):
        title = response.xpath('.//h1/i/text()').extract_first()
        logo = 'https://upload.wikimedia.org/wikipedia/en/5/56/Dragon_quest_logo.png'
        slime = 'https://upload.wikimedia.org/wikipedia/en/1/13/Slime_%28Dragon_Quest%29.jpg'
        print(DQItem(title=title, logo=logo, slime=slime))
        yield DQItem(title=title, logo=logo, slime=slime)

def get_settings() -> Settings:
    """create and return a scrapy settings object"""
    settings = Settings()
    # get current working directory
    cwd = str(pathlib.Path().absolute())
    # set path in which to store images
    settings.set('IMAGES_STORE', cwd + '\\')
    settings.set('IMAGE_URL_FIELDS', {
        'logo': {
            'name_field': 'title',
            'sub_folder': 'logos',
            'path_field': 'logo_path',
        }, 'slime': {
            'name_field': 'title',
            'sub_folder': 'slimes',
            'path_field': 'slime_path',
        }
    })
    # enable the pipeline
    settings.set('ITEM_PIPELINES', {
        'pipeline.ImageNamePipeline': 200
    })
    return settings

if __name__ == '__main__':
    # routine to run scrapy from a script
    # see: https://docs.scrapy.org/en/latest/topics/practices.html#run-scrapy-from-a-script
    settings = get_settings()
    runner = CrawlerRunner(settings)
    d = runner.crawl(DQSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
