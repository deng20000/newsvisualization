import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError, TCPTimedOutError
from ..items import ScraperItem


class ExampleSpider(scrapy.Spider):
    # Name of the spider
    name = "dig"
    # Domains to be allowed
    allowed_domains = ["dig.watch"]

    def start_requests(self):
        # Base URL for the website
        base_url = "https://dig.watch/updates"
        # Total number of pages to be scraped
        total_pages = 5  # Specify the total number of pages you want to scrape

        # Generate the start URLs for all the pages
        start_urls = [f"{base_url}?_paged={page_number}" for page_number in range(1, total_pages + 1)]

        # Iterate through the start URLs and yield a request for each
        for index, url in enumerate(start_urls):
            yield scrapy.Request(url=url,
                                 callback=self.parse,
                                 errback=self.errback_func,
                                 meta={'index': index})

    # seize the hot topic in Chinese Website News into Mongodb
    def get_topic_parse(self, response, **kwargs):
        pass

    def parse(self, response, **kwargs):
        # First and last title numbers
        fir_title, las_title = 1, 11
        # Iterate through the titles
        for title_number in range(fir_title, las_title):
            # Yield the title, link, description and date
            one_new = ScraperItem()

            # get title
            one_new['new_title'] = response.xpath(f"//div[{title_number}]/div/h3/a/text()").get()
            # get deputy_title
            one_new['new_deputy_title'] = response.xpath(f"//div[{title_number}]/div/p/text()").get()
            # get image
            one_new['new_image'] = response.xpath(f"//*[@id='primary']/section/div[1]/div[{title_number}]/a/img/@src").get()
            # get date
            one_new['new_date'] = response.xpath(f"//*[@id='primary']/section/div[1]/div[{title_number}]/div/div/text()").get()
            # get link
            one_new['new_link'] = response.xpath(f"//div[{title_number}]/div/h3/a/@href").get()
            yield one_new

    def errback_func(self, failure):
        # Check for HttpError
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url)

        # Check for DNSLookupError
        elif failure.check(DNSLookupError):
            request = failure.request
            self.logger.error("DNSLookupError on %s", request.url)

        # Check for TimeoutError and TCPTimedOutError
        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error("TimeoutError on %s", request.url)

