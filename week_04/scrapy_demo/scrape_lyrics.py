"""
Install:
-----------
conda install -c conda-forge scrapy

How to Run:
-----------
scrapy runspider -L WARNING -o data.csv scrape_lyrics.py

Background:
-----------
https://elitedatascience.com/python-web-scraping-libraries

"""

# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re


class LyricsSpider(scrapy.Spider):
    name = 'lyrics_bot'
    allowed_domains = ['www.metrolyrics.com']
    start_urls = ['http://www.metrolyrics.com/top-artists.html/']

    custom_settings = {
        'DEPTH_LIMIT': 2,
        'ROBOTSTXT_OBEY':True,
        'DOWNLOAD_DELAY': 0.3
    }

    def clean(self, lyricstext):

        lyricstext = ' '.join(lyricstext)
        lyricstext = re.sub('\n|\r|\t|\\|\,|\'|\"|\,|\*', '', lyricstext)
        lyricstext = re.sub('\-|\:|\)|\(|\[|\]|\{|\}|\.|\!', ' ', lyricstext)
        lyricstext = re.sub('\s+', " ", lyricstext)
        return lyricstext

    def parse(self, response):

        artists = response.xpath('//a[@class="image"]/@href').getall()

        for a in artists:
            yield Request(a)

        songs = response.xpath('//td/a/@href').getall()
        for s in songs:
            yield Request(s)

        title = response.xpath('//div[@class="banner-heading"]/h1/text()').get()
        # text = response.xpath('//div[@id="lyrics-body-text"]//text()').getall()
        text = response.xpath('//div[@class="lyrics-body"]//p[@class="verse"]\
        /text()').getall()
        text = self.clean(text)

        #check if any are empty
        if title and text:
            print(title)
            print(text)
            item = {'lyrics': text, 'title': title}
            yield item
        else:
            pass
