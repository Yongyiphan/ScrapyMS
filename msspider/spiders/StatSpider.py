from tqdm import tqdm
from pathlib import Path
import scrapy


class ExpSpider(scrapy.Spider):
    tag = "Stats"
    name = "Exp"

    def start_requests(self):
        urls = []
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        ...

    ...
