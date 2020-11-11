# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
import json

class ScraperPipeline:
    def json_extract(self, obj, key):
        """Extract nested values from a JSON tree."""
        """Recursively fetch values from nested JSON."""
        arr = []

        def extract(obj, arr, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == key:
                        arr.append(v)
                        
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        values = extract(obj, arr, key)
        return values

    def process_item(self, item, spider):
        js = item['JS']
        # clean up start
        js = re.sub(r'^window\.__WEB_CONTEXT__\s*=\s*{', r'{', js)
        # clean up end
        js = re.sub(r'};\(this\.\$WP.+$', r'}', js)
        # add double-quote to "pageManifest" to make it a key
        js = js.replace('pageManifest', '"pageManifest"')

        # only get the part where key = "reviewListPage", which contains review info
        js = json.loads(js)
        js = self.json_extract(js, 'reviewListPage')[0] #only 1 "reviewListPage" should exist
        #js = json.dumps(js) #Commented out cause We would output to JSON directly

        return {'Review_JSON': js}