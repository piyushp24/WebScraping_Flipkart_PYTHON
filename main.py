import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

product_name = []
Prices = []
description = []
reviews = []
    


# 2 to 12 means 10 pages
for i in range(1,200):  
      
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i) # flipkart website se url chahiye hoga kyuki ham http request bhejege

    r = requests.get(url)            
    #print(r)
    if r.status_code == 200:
        soup = bs(r.text, "lxml")
        # now we are getting the whole page html (data) now in reviews, there is a section reviews for popular mobiles, 
        # so reviews will become 39 instead of 24, it is also including the reviews of those mobiles

        box = soup.find("div",class_="DOjaWF gdgoEp")

        if box:
            names = box.find_all("div", class_ = "KzDlHZ")
            for i in names:
                name = i.text
                product_name.append(name)

    # print(product_name)

            pri = box.find_all("div", class_ = "Nx9bqj _4b5DiR")
            for i in pri:
                pr = i.text
                Prices.append(pr)

    # print(Prices)

            desc = box.find_all("ul", class_="G4BRas")
            for i in desc:
                des = i.text
                description.append(des)

    # print(description)

            revs = box.find_all("div", class_="XQDdHH")
            for i in revs:
                rev = i.text
                reviews.append(rev)
    
    else:
        print(f"failed to retrieve page {i}")

    # print(reviews)


min_length = min(len(product_name), len(Prices), len(description), len(reviews))

df = pd.DataFrame({"Product Name" : product_name[:min_length], "Prices":Prices[:min_length], "Description":description[:min_length], "Rating":reviews[:min_length]})
df.to_csv("C:/Users/DELL/OneDrive/Desktop/web_scraping2/flipkart_phones_under_50000.csv", index = False)



print(len(box))
print(len(product_name))
print(len(Prices))
print(len(description))
print(len(reviews))