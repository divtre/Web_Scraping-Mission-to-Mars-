import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import pandas as pd
import requests
import time
from splinter import Browser
from bs4 import BeautifulSoup
import pymongo


# Initialize browser
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_mars():
# Initialize browser
    mars={}
    browser = init_browser()
    #######################scraping title and news########################
    url_mars_nasa = 'https://mars.nasa.gov/news/'
    browser.visit(url_mars_nasa)
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    
    news_title = news_soup.find_all('div', class_='content_title')[0].text
    news_p=news_soup.find_all('div', class_='article_teaser_body')[0].text

    #######################scraping img url##################################3
    url_mars_nasa_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_mars_nasa_img)
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    mars_img = news_soup.find_all('a', class_='button fancybox')
    mars_img_url_1=mars_img[0]['data-fancybox-href']
    mars_img_url='https://www.jpl.nasa.gov'+mars_img_url_1
    print(mars_img_url_1)
    print(mars_img_url)

    ###########################scraping facts#################################3
    url_facts = 'https://space-facts.com/mars/'
    tables = pd.read_html(url_facts)
    df = tables[0]
    df.columns = ["Description","Value"]
    df=df.set_index("Description")
    html_table = df.to_html()
    html_table=html_table.replace('\n', '')
    ##########################scraping weather###############################
    url_mars_weather = 'https://twitter.com/marswxreport?lang=en'
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path)
    browser.visit(url_mars_weather)

    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    text=news_soup.find_all('div', class_='js-tweet-text-container')[0].text
    text=text.replace('\n', '')
    ###########################################

    mars = {
        "news_title": news_title,
        "news_p": news_p,
        "img": mars_img_url,
        "facts": html_table,
        "weather":text
    }
    print("1234")
    #pprint.pprint(mars)
    # Return results
    return mars
