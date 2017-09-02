#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'MICROYU'

from bs4 import BeautifulSoup
import requests

def getWeather(city, number):
    url = 'http://tianqi.2345.com/' + city + '/' + number + '.htm'
    html = requests.get(url)
    Soup = BeautifulSoup(html.text, 'html.parser')
    weather = Soup.select('#wrap > div.tday-live.module.clearfix > div.meta > div.unit-1 > div.charact > div > a')
    now_temp = Soup.select('#weaLiveInfo > ul > li:nth-of-type(1) > i')
    humidity = Soup.select('#weaLiveInfo > ul > li:nth-of-type(2) > i')
    wind = Soup.select('#weaLiveInfo > ul > li:nth-of-type(3) > i')
    pressure = Soup.select('#weaLiveInfo > ul > li:nth-of-type(4) > i')
    sun_raise = Soup.select('#weaLiveInfo > ul > li:nth-of-type(5) > i')
    sun_down = Soup.select('#weaLiveInfo > ul > li:nth-of-type(6) > i')

    return {'weather':weather[0].get_text(),'now_temp':now_temp[0].get_text(),'humidity':humidity[0].get_text(),'wind':wind[0].get_text(),'pressure':pressure[0].get_text(),'sun_raise':sun_raise[0].get_text(),'sun_set':sun_down[0].get_text()}

#print(weather('xian', '57036'))