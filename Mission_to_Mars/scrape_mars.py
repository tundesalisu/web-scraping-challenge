from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrapeData():
    browser = init_browser()
    listings = {}

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    scraped_data = soup.find_all('div', class_='item')

    title = []
    img_url = []
    img_title_dict = {}
    img_title_dict_list = []
    for each in scraped_data:
        each_title = 'https://astrogeology.usgs.gov'+ each.img['src']
        each_title_text = each.h3.text
        img_url.append(each_title)
        title.append(each_title_text)
        img_title_dict['title']= each_title_text
        img_title_dict['img_url']= each_title
        img_title_dict_list.append(img_title_dict)
    print(img_title_dict_list)


    # listings["headline"] = soup.find("a", class_="result-title").get_text()
    # listings["price"] = soup.find("span", class_="result-price").get_text()
    # listings["hood"] = soup.find("span", class_="result-hood").get_text()

    return img_title_dict_list
#successfully able to scrape data.
#scrape()