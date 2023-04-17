import scrapy


class WindyFSpider(scrapy.Spider):
    name = "windy_f"
    allowed_domains = ["app.gooooal.com"]
    start_urls = ["http://app.gooooal.com/"]

    def parse(self, response):
        pass
