import scrapy
from scrapy.http import Request
from jobSpider.items import JobspiderItem

class JobSpider(scrapy.spiders.Spider):
    name = 'jobSpider'
    allowed_domains = ["liepin.com"]
    start_urls = [
        # 定义初始链接为猎聘网中以Python为关键词的搜索结果页面
        "https://www.liepin.com/zhaopin/?key=java",
    ]

    def parse(self, response):
        for sel in response.xpath('//ul[@class="sojob-list"]/li//div[@class="sojob-item-main clearfix"]'):
            # 提取列表界面中的招聘关键信息
            item = JobspiderItem()
            item['title'] = str(sel.xpath('div/h3/a/text()').extract())[32:][:-3]
            item['salary'] = str(sel.xpath('div/p/span[@class="text-warning"]/text()').extract())[2:][:-2]
            item['link'] = str(sel.xpath('div/h3/a/@href').extract())[2:][:-2]
            item['city'] = str(sel.xpath('div/p/a[@class="area"]/text()').extract())[2:][:-2]
            item['edu'] = str(sel.xpath('div/p/span[@class="edu"]/text()').extract())[2:][:-2]
            item['experience'] = str(sel.xpath('div/p/span/text()').extract()[2])
            item['company'] = str(sel.xpath('div[@class="company-info nohover"]/p/a/text()').extract())[2:][:-2]
            yield item

        # 判断有无下一页内容
        # 获取底部页码链接元素
        pageLink = response.xpath('//div[@class="pagerbar"]/a/@href').extract()
        if len(pageLink) >= 7:
            nextPage = pageLink[len(pageLink)-2]
        if len(nextPage) > 15:
            yield Request(url=nextPage,callback=self.parse)
        else:
            print('No next page! Job is done!')