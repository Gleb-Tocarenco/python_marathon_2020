import scrapy

class CarsSpider(scrapy.Spider):

    name = 'cars'

    def start_requests(self):
        urls = [
            'https://999.md/ru/66826567',
            'https://999.md/ru/66662305',
            'https://999.md/ru/66994735'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'title': response.xpath('//*[@id="container"]/div/section/header/h1/text()').get(),
            'price': response.css('.adPage__content__price-feature__prices__price__value::text').get(),
            'phone': ','.join(response.css('.adPage__content__phone a::attr(href)').getall()),
            'region': ','.join(response.css('.adPage__content__region dd::text').getall()).strip()
        }