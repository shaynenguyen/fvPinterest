import requests, re
from scrapy.selector import Selector
import pandas as pd

# Database Stuff
from database import engine
from models import Images

# Initialize
website = 'https://www.pexels.com/'
list_image_url = []
listName, listWidth, listHeight = ([] for i in range(3))

# Cleaning Regex
regex_url_suffix = r"(\?[^\s]+)"
regex_image_suffix = r"$(png|jpeg)"


# XPath Expression
xpath_dictionary = {
    'name'  :           r"//div[@class='photos__column']/div/article/a/img/@alt",
    'images':           r"//div[@class='photos__column']/div/article/a/img/@src",
    'height':           r"//div[@class='photos__column']/div/article/a/img/@data-image-height",
    'width' :           r"//div[@class='photos__column']/div/article/a/img/@data-image-width"
}


# Connect to website
res = requests.get(website)

# Check return header
if res.status_code == 200:

    # Initialize
    xpath_selector  = Selector(text= res.text)

    # Push to list
    listName.extend(xpath_selector.xpath(xpath_dictionary['name']).extract())
    list_image_url.extend(xpath_selector.xpath(xpath_dictionary['images']).extract())
    listWidth.extend(xpath_selector.xpath(xpath_dictionary['width']).extract())
    listHeight.extend(xpath_selector.xpath(xpath_dictionary['height']).extract())

    print("Total added: ", len(list_image_url))
    print(list_image_url[0:10])
    print("\n")
    print(listName)
    print("\n")
    print(listHeight)
    print("\n")

# Quick clean up
list_image_url = ['' if (url.find("avatar") != -1) and (url.find("jpeg") == 0) else url for url in list_image_url]
list_image_url = [re.sub(regex_url_suffix,"",url) for url in list_image_url]
print(list_image_url)

# To Dataframe
df = pd.DataFrame(zip(listName, list_image_url, listWidth, listHeight), columns=['name','url','width','height'])

df.dropna(subset=['url'])

df.to_sql(name='images', con=engine, if_exists='replace', index=True)
df.info()