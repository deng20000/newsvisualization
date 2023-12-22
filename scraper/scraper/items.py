# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# Define a ScraperItem class that inherits from scrapy.Item
class ScraperItem(scrapy.Item):

    # define the fields for your item here like:
    # 标题
    new_title = scrapy.Field()
    # 副标题
    new_deputy_title = scrapy.Field()
    # 图像
    new_image = scrapy.Field()
    # 时间
    new_date = scrapy.Field()
    # 链接
    new_link = scrapy.Field()
    # 内容
    # new_content = scrapy.Field()


