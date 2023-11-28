import requests
from bs4 import BeautifulSoup
import csv
# url="https://foodmandu.com/"
# r= requests.get(url)
# # print(r.text)
# source_code= r.text
# # with open('sc.txt','w') as file_obj:
# # 	file_obj.write(f"{source_code}")
# 
# soup= BeautifulSoup(source_code)
# listing_div = soup.findAll("div",{
# 	"class":"listing"})
# # print(listing_div)
# for listing in listing_div:
#  	print(listing.text.strip())

# url2="https://foodmandu.com/Restaurant/Details/289"
# r2= requests.get(url2)
# # print(r2.text)
# code=r2.text
# soup = BeautifulSoup(code)
# listing_menu= soup.findAll("ul",{
# 	"class":"menu__content wrap"
# 	})
# print (listing_menu)
# for listing in listing_menu:
#     print("/n",listing.text.strip())
class FoodmanduScrapper:
	def __init__(self):
		self.url="https://foodmandu.com/webapi/api/v2/Product/GetVendorProductsBySubCategoryV2?VendorId={resturant_id}&show="
		pass


	def scrap_menu(self, resturant_id):
		url= self.url.format(resturant_id=resturant_id)
		req= requests.get(self.url)

		all_menu= req.json()

		print(req.text)

		all_menus = all_menus[0]['items']
		optput= []

		for menus in all_menus:
			print("name:",menu['name'],menu['price'])
			tmp={
				"name": menu['name'],
				"price": menu['price']
			}
			output.append(tmp)
		headers = output[0].keys()
		with open('foodmandu_menus.csv','w') as file_obj:
			dict_writer= csv.DictWriter(file_obj,headers)
			dict_writer.writeheader()
			dict_writer.writerows(output)

		return all_menus

S=FoodmanduScrapper()
S.scrap_menu(1027)



