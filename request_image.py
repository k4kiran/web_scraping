import requests 
image_url = "https://live.staticflickr.com/8519/8620325735_5cb816e47d_m.jpg"
r = requests.get(image_url)
with open("image" + count +".jpg",'wb') as f: 
    f.write(r.content) 