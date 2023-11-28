import requests
from bs4 import BeautifulSoup
url="https://foodmandu.com/Restaurant/Details/1027"

r=requests.get(url)
# print(r.text)
# print (r.text)
source_code=r.text
# print(source_code)
soup= BeautifulSoup(source_code,features="html.parser")
print(soup.text)
# print(soup.findAll("div", {"class":"small dim"}))
# # listing_div = soup.findAll("div", {"class":"small dim"})
# # for listing in listing_div:
# #  	print(listing.text.strip())
# #  	print (5)
