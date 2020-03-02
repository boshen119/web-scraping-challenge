from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import time
import re


def mars_news(browser):
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    # Get first list itema nd wait half a second if not immediately present
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=0.5)

    html = browser.htmlnews_soup = BeautifulSoup(html, "html.parser")

    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")
        news_title = slide_elem.find("div", class_="content_title").get_text()
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None 
    return news_title, news_n

def featured_image(browser):
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    # Find and click the full images button
    full_image_elem = browser.find_by_id("full_image")
    full_image_elem.click()

    # Find the info button and click that
    browser.is_element_present_by_text("more info", wait_time=0.5)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = BeautifulSoup(html, "html.parser")

    # Find the relative image url
    img = img_soup.select_one("figure.lede a img")

    try:
        img_url_rel = img.get("src")
    except AttributeError:
        return None
    
    # Use the base url to create an absolute url
    img_url = f"https://www.jpl.nasa.gov{img_url_rel}"

    return img_url

def hemisphere(browser):
    return

def twitter_weather(browser):
    return

def scrape_hemisphere(html_text):

    return

def mars_facts():
    try:
        df = pd.read_html("https://space_facts.come/mars/")[0]
    except BaseException: 
            return None
    df.columns = ["description", "value"]
    df.set_index("description", inplace=True)
    
    return df.to_html(classes="table table-striped")


def scrape_all():
    executable_path = {'executable_path': '/Users/Bons/Downloads/chromedriver'}
    browser = Browser('chrome', executable_path="chromedriver", headless=False)
    
    news_title, news_paragraph = mars_news(browser)

    data = {
        "news_title" : news_title,
        "news_paragraph" : news_paragraph,
        "featured_img" : featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    browser.quit()
    return data


if __name__ == "__main__":
# if running as a script, print scraped data
    print(scrape_all())