from bs4 import BeautifulSoup
import requests
import re

divar = requests.get("https://divar.ir/s/tehran")
src = divar.text
soup = BeautifulSoup(src, "html.parser")
# print(soup.prettify())
ads = soup.findAll("div", attrs={
    "class" : "kt-post-card__body"
})

for ad in ads:
    description = ad.find(
        "div",
        attrs={
            "class" : "kt-post-card__description"
        }
    )
    if not description == None:
        #print(description.text, end="\n")

        if "توافقی" in description.text:
            #print(description.text, end="\n")
            price = "توافقی"
            title = ad.find(
                "div",
                attrs={
                    "class" : "kt-post-card__title"
                }
            )
            #print(title.text)

            ad_bottom = ad.find(
                "div",
                attrs={
                    "class" : "kt-post-card__bottom"
                }
            )
            #print(ad_bottom.text)

            print(f"Title : {title.text} \nPrice : {price} \nAdvertiser : {ad_bottom.text} \n______________\n")


        # else:
        #     continue