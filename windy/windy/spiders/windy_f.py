import scrapy
from .. import items

class WindyFSpider(scrapy.Spider):
    name = "windy_f"
    allowed_domains = ["app.gooooal.com"]
    start_urls = ['http://app.gooooal.com/footBallDataBaseAction.do?method=doFootBallDataBase']

    def parse(self, response):
        # 提取每个联赛的URL
        league_urls = response.xpath('//a[contains(text(), "意甲")]/@href')  # /competition.do?lid=5&sid=2022&pid=23&lang=tr
        for league_url in league_urls:
            yield scrapy.Request(url = self.allowed_domains + league_url, callback=self.parse_season)

    def parse_season(self, response):   # http://app.gooooal.com/resultschedule.do?lid=5&sid=2022&lang=tr
        # 提取每个赛季的URL
        season_urls = response.xpath('//a[@class="font_weight_normal"]/@href')
        for season_url in season_urls:
            yield scrapy.Request(url=season_url, callback=self.parse_match)

    def parse_match(self, response):
        # 提取每场比赛的相关信息，生成item
        item = items.WindyItem()
        item['home_team'] = ...
        item['away_team'] = ...
        item['score'] = ...
        yield item
