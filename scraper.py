#Scraping the site
from bs4 import BeautifulSoup
import requests

download_links = []
for year in range(2000, 2021):
    main_url = "https://bulkdata.uspto.gov/data/patent/grant/redbook/fulltext/{}/".format(year)
    re = requests.get(main_url)
    soup = BeautifulSoup(re.text, "html.parser")
    links = soup.find_all("a")
    hrefs = []
    for link in links:
        if "zip" in link["href"]:
            download_link = main_url+link["href"]
            download_links.append(download_link)
            print(download_link)

#Downloading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
from webdriver_manager.chrome import ChromeDriverManager
import time

#Sleep for 5 seconds between as to not overload their servers and get denied
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
for i in download_links[:3]:
    try:
        print("Attempt to Download {}".format(i))
        driver.get(i)
        time.sleep(5)
        print("Successfully Downloaded {}".format(i))
    except:
        print("Failed {}, sleeping for 30 seconds.".format(i))
        time.sleep(30)
        print("Retrying: {}".format(i))
        driver.get(i)
        time.sleep(30)