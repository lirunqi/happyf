import scrapy
from .. import items
import re

class WindyFSpider(scrapy.Spider):
    name = "windy_f"
    allowed_domains = ["app.gooooal.com"]
    start_urls = ['http://app.gooooal.com/footBallDataBaseAction.do?method=doFootBallDataBase']

    def parse(self, response):
        # 提取每个联赛、每个赛季的URL
        for lid in range(1, 6):
            for sid in range(2011, 2024):
                result_urls = "/resultschedule.do?lid=" + str(lid) + "&sid=" + str(sid) + "&lang=hanz"
                yield scrapy.Request(url="http://app.gooooal.com" + result_urls, callback=self.parse_season)

    def parse_season(self, response):
        # 提取当前赛季、联赛的盘口URL
        odd_urls = response.xpath('//a[contains(@href, "javascript:toOddsDetail(")]/@href')
        for mid in odd_urls:
            mid = re.search(r"mid=(\d+)", mid.extract_first()).group(1)
            yield scrapy.Request(url="http://app.gooooal.com/fb_detail.html?mid=" + mid + "&cid=1001&ms=0&lang=cn", callback=self.parse_match)

    def parse_match(self, response):
        # 提取每场比赛的相关信息，生成item
        print('oook')
        print(response)
        # item = items.WindyItem()
        # item['home_team'] = ...
        # item['away_team'] = ...
        # item['score'] = ...
        # yield item
