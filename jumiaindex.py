""" bs4 scraper for jumia"""
import bs4 as bs
import urllib.request as urlr
"""
userstring -> jumia.com/catalog/?q={}.format(userstring)
"""
search = "laptops"
st =["laptops","laptop"]
if search in st:
    jumURL="https://www.jumia.com.ng/laptops/?sort=lowest-price&rating=2-5#catalog-listing"
else:
    jumURL="https://www.jumia.com.ng/catalog/?q={}#catalog-listing".format(st)

site = urlr.Request(jumURL, headers={'User-Agent':'Mozilla/5.0'})
# source = urlr.urlopen("https://books.toscrape.com/").read()
source = urlr.urlopen(site,timeout=20).read()
soup = bs.BeautifulSoup(source,'lxml')


body = soup.body

def jumia():
    ## this should be a dictionary or json
    products = []
    prdlist = body.find_all(class_="prd _fb col c-prd")
    for i in range(len(prdlist)):
        
        plink = prdlist[i].find(class_="core", href=True)
        link = plink.get("href")
        
        price = plink.find(class_="prc").find(text=True)
        img = plink.find("img",class_="img")["data-src"]
        pname = plink.get("data-name")
        
        products.append({"name":pname,"Link":link,"Price":price,"image":img})
        
        # price = "prc"
        # product_name = "data-name"
        # image = data-src 
    # return(products[0].get("name"))
    return products
laptops = jumia()
print(laptops[0])
# lap = []
# for i in laptops:
#     print(i["name"])



