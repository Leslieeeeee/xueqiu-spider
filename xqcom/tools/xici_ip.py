# -*- coding: utf-8 -*-

import requests
from scrapy.selector import Selector
def crawl_ips():
    headers = {"User-Agent = "}
    request = requests.get("http://www.xicidaili.com/")

    selector = Selector(text=request.text)
    all_trs = selector.css("#ip_lsit tr")

    ip_list = []

    for tr in all_trs[1:]:
        speed_str = tr.css(".bar::attr(title)").extract()[0]
        if speed_str:
            speed = float(speed_str.split("秒")[0])
        all_texts = tr.css("td:text").extract()

        ip = all_texts[0]
        port= all_texts[1]
        proxy_type = all_texts[5]

        ip_list.append((ip, port, proxy_type, speed))


