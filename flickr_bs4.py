import requests
import cssutils
from bs4 import BeautifulSoup
import re
import logging
from time import sleep

#url of flickr page
url = "https://www.flickr.com/search/?text=animals"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
#print(soup.prettify)

imagediv = soup.findAll('div',class_ = "awake")
print(soup.select('.awake'))
print(len(imagediv))
#print(imagediv)
#imagediv = imagediv.findAll('div',class_ = "photo-list-photo-interaction")
#newdiv = imagediv.findAll('background-image')
images = []

#imagediv = soup.findAll('div',{'class': ['view','awake']})
#print(imagediv)
'''
for i in range(0,20):
    image1 = imagediv[i]['style']
    cssutils.log.setLevel(logging.CRITICAL)
    style = cssutils.parseStyle(image1)
    url = style['background-image']
    url = re.sub('url\(', '', url)
    url = re.sub('\)', '', url)
    images.append(url)
for image in images:
    print(image)
'''
'''
start = image1.find("url(")
end = image1.find("g)")
print(start,end)
'''