# This file will contain the Scrapy scraper used to scrape IMDB

import scrapy

# Gives the table and row of cast_list table in Scrapy shell (not finished)
table = response.xpath('//*[@class="cast_list"]//tr')
row = table[1]
row.xpath('td//text()').extract()