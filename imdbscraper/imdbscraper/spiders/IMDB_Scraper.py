# This file will contain the Scrapy scraper used to scrape IMDB
'''
# Gives the table and row of cast_list table in Scrapy shell (not finished)
table = response.xpath('//*[@class="cast_list"]//tr')
row = table[1]
# Gives the actor's name. The problem is some rows only have 3 indices,
# so we get an IndexError. My initial thought it to have a try/except statement.
# This could cause long term problems though, so I may extract from the table 
# by skipping by 2 each time, starting at 1
row.xpath('td//text()')[3].extract()

# Loop to extract the name from cast_list table.
# In testing with Scrapy shell, the rows without a position of 2 were skipped
for row in response.xpath('//*[@class="cast_list"]//tr'):
    name = row.xpath('td[2]//text()').extract()
    print(name)
'''
import scrapy
from imdbscraper.items import ImdbscraperItem
 
class CastListSpider(scrapy.Spider):
    name = 'cast_list'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/title/tt1439629/fullcredits?ref_=tt_ql_1']
 
 
    def start_requests(self):
        urls = [
            'https://www.imdb.com/title/tt1439629/fullcredits?ref_=tt_ql_1',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        cast = ImdbscraperItem()
        cast['names'] = []
        for row in response.xpath('//*[@class="cast_list"]//tr'):
            cast.append(row.xpath('td[2]//text()').extract())
        yield cast