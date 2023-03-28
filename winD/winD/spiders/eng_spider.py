import scrapy
from scrapy.crawler import CrawlerProcess

class OddsSpider(scrapy.Spider):
    name = 'odds'
    start_urls = ['https://www.oddsportal.com/soccer/england/premier-league/']

    def parse(self, response):
        for match in response.css('td.name.table-participant'):
            yield {
                'match': match.css('a::text').get(),
                'odds': match.xpath('following-sibling::td')[1].css('a::text').get()
            }

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(OddsSpider)
    process.start()
