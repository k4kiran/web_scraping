
#importing required libraries
import requests
import cssutils
import re
import logging
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#getting url and scrolling down pages
try:
    count = 0
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options = options)
    keyword = "animals"
    driver.get(f'https://www.flickr.com/search/?text= {keyword}')
    for i in range(0,50):
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        try:
            if driver.find_elements_by_css_selector('.no-outline'):
                driver.find_elements_by_css_selector('.no-outline').click()
        except Exception as e:
            print("load more not yet appeared...")
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        temp_imagediv = soup.findAll('div',class_ = "awake")
        print("fetching page " + str(i+1) + " of flickr.....")
        print("fetched " + str(len(temp_imagediv)) + " images so far...")
        sleep(20)

except Exception as e:
    print("error searching" + str(e))

#parsing the content to bs4 object
try:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    imagediv = soup.findAll('div',class_ = "awake")
    image_count = len(imagediv)
    print(image_count)
    images = []
    
    #getting the element and preprocessing
    for i in range(0,image_count):
        image1 = imagediv[i]['style']
        cssutils.log.setLevel(logging.CRITICAL)
        style = cssutils.parseStyle(image1)
        url = style['background-image']
        url = re.sub('url\(', 'https:', url)
        url = re.sub('\)', '', url)
        images.append(url)

    #downloading each image to folder
    for image in images:
        count = count + 1
        image_url = str(image)
        r = requests.get(image_url)
        with open("flickr_dataset/image" + str(count) +".jpg",'wb') as f: 
            f.write(r.content) 
            print("downloading image"+ str(count) + ".....")
            print(image)

    '''
    images = driver.find_elements_by_class_name("view")
    print(images)
    print("size is :" + len(images))
    sleep(5)
    '''
except Exception as e:
    print(str(e))



'''
#url of flickr page
url = "https://www.flickr.com/search/?text=animals"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
#print(soup.prettify)

imagediv = soup.findAll('div',class_ = "awake")
#print(imagediv)
#imagediv = imagediv.findAll('div',class_ = "photo-list-photo-interaction")
#newdiv = imagediv.findAll('background-image')
images = []

#imagediv = soup.findAll('div',{'class': ['view','awake']})
#print(imagediv)

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