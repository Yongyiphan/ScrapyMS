import time
from time import sleep
import os
from scrapy.utils.log import configure_logging

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner

# Custom Includes
from msspider.spiders import StatSpider
import utils as utils


def Run(path):
    start = time.time()
    DataTempPath = os.path.join(path, "TempData")
    utils.M["StorePath"] = DataTempPath
    if not os.path.exists(DataTempPath):
        os.mkdir(DataTempPath)
        print("Created Temp Data Folder")

    for cat in utils.Data_Categories:
        tPath = os.path.join(DataTempPath, cat)
        if not os.path.exists(tPath):
            print(f"Created {cat} Folder")
            os.mkdir(tPath)

        ...

    runner = CrawlerRunner()
    StatsCrawl(runner)

    runner.join().addBoth(lambda _: reactor.stop())
    reactor.run()

    end = time.time()
    print(f"Process complete in {end - start}")

    ...


def StatsCrawl(crawler):
    StatSpiders = {
        name: cls for name, cls in StatSpider.__dict__.items() if isinstance(cls, type)
    }
    for name, s in StatSpiders.items():
        if "spider" in name.lower():
            crawler.crawl(s)
    ...


if __name__ == "__main__":
    Cwd = os.path.abspath(os.getcwd())
    Run(Cwd)
