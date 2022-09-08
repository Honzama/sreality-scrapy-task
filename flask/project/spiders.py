import json
import re

import scrapy


class FlatsSpider(scrapy.Spider):
    name = 'flats'
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=0&per_page=500']

    def parse(self, response, **kwargs):
        response_json = json.loads(response.body)
        for flat in response_json.get('_embedded').get('estates'):
            yield (
                {
                    'title': re.sub(r'\s', ' ', flat.get('name')),
                    'image_url': flat.get('_links').get('images')[0].get('href'),
                }
            )
