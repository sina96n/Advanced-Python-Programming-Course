from bs4 import BeautifulSoup
import mysql.connector as mysql
import requests
import re


def digikala_search(search):
    # digikala search algorithm
    digikala = requests.get(f"https://www.digikala.com/search/?q={search}")

    src  = digikala.text
    # creating soup object for the given page
    soup = BeautifulSoup(src, "html.parser")
    # extracting search results from page
    contents = soup.find_all("div", attrs={
        "class" : "c-product-box__content"
    })

    for content in contents:
        title = content.find("a", attrs={
            "class" : "js-product-url"
        })

        status = content.find("div", attrs={
            "class" : "c-product-box__rate-status"
        })
        status_lst = re.findall(r"(\d\.*\d*)\s*\((\d*)\)\s*(.*)\s*", status.text)

        price_row = content.find("div", attrs={
            "class" : "c-price__value-wrapper"
        })
        price_info = re.sub(r"[\s\n\t]", "", price_row.text)

        # printing output (optional)
        # print(
            # f"{title.text}\nRating : {status_lst[0][0]} ({status_lst[0][1]})\nStatus: {status_lst[0][2]}\nPrice : {price_info}", 
            # end="\n_______________________________________________"
        # )




        # Saving result into dataabase
        # DataBase Structure : 

        ## |         name          | rating | number of ratings |        Price       |          Status          |

        ## |    Galaxy Buds Live   |  4.2   |        1988       |  موجود در انبار   |   1,899,000 تومان       | 

        # creating connection to database
        con = mysql.connect(
            user="username",
            password="password",
            database="market"
        )
        # creating a cursor
        cur = con.cursor()
        # writing query to add data to database 
        query = "Insert into digikala(name, rating, n_rating, status, price) values('{}', '{}', '{}', '{}', '{}')".format(
            title.text,
            status_lst[0][0],
            status_lst[0][1],
            status_lst[0][2],
            price_info
        )

        cur.execute(query)
        # applying changes
        con.commit()
        # closing connection
        con.close()

search = input("Search Digikala : ").replace(" ", "-")
digikala_search(search)




# By Sina Kazemi
# https://github.com/sina96n