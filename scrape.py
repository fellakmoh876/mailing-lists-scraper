import logging
import os
import pandas as pd
import re
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from googlesearch import search

logging.getLogger('scrapy').propagate = False

# extract websites from google with googlesearch
def get_urls(tag, n, language):
    urls = [url for url in search(tag, stop=n, lang=language)][:n]
    return urls

get_urls('movie rating', 5, 'en')

# make a regex expression to extract emails
mail_list = re.findall('\w+@\w+\.{1}\w+', html_text)