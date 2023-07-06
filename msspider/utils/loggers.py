from scrapy.utils.log import configure_logging, _get_handler, TopLevelFormatter

import datetime
import logging
import time


class SMSTopLevelFormatter(TopLevelFormatter):
    def __init__(self, loggers=None, name=None):
        self.loggers = loggers or []
        self.name = name
        ...

    def filter(self, record):
        return super().filter(record)

    ...


def log_init(name: str):
    ...
