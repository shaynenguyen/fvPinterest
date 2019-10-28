import requests
from scrapy.selector import Selector
from PIL import Image

# Initialize
website = 'https://www.pexels.com/'
regex_image = ''
list_image_url = []
listWidth, listHeight = ([] for i in range(2))


# XPath Expression
xpath_dictionary = {
    'images':           r"//div[@class='photos__column']/div/article/a/img/@src"
}


# Connect to website
res = requests.get(website)

# Check return header
if res.status_code == 200:

    # Initialize
    xpath_selector  = Selector(text= res.text)

    # Push to list
    list_image_url.extend(xpath_selector.xpath(xpath_dictionary['images']).extract())

    print("Total added: ", len(list_image_url))
    print(list_image_url[0:10])

# for iurl in list_image_url:
#     with Image.open(iurl) as i:
#         tempDetail = i.size
#         listWidth.append(tempDetail[0])
#         listHeight.append(tempDetail[1])