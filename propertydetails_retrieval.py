import html

import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import brotli
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive"
}

driver = webdriver.Chrome()
driver.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Bhubaneswar&category=B&parameter=rel&hideviewed=N&ListingsType=I&filterCount=3&incSrc=Y&fromSrc=homeSrc")

driver.implicitly_wait(5)

html_content = driver.page_source

with open("property_details.html", "w", encoding="utf-8") as file:
    file.write(html_content)


driver.quit()

print("HTML page saved as property_details.html")