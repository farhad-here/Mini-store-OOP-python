# import section
from models import Product
import json
'''
This is store.py
represent a store which contains the products
'''
# class
class Store:
       '''
       class store for store which include product and 
       add products and
       list of product and
       find products
       '''
       # list of product object
       def __init__(self):
              # product with name price stock (list)
              self.products = []
       
       # method add product -> name price stock
       def add_product(self,name:str,price:float,stock:int,user:str,timer:str):
              '''
              add new product to the store
              if product exist so just update the price and stock
              '''
              # find about if product exist or not (searching by the name)
              exist_product = self.find_products(name=name)
              if exist_product:
                     for i in self.products:
                            if i.name.lower() == name.lower():
                                   # change price in json
                                   i.price = price
                                   # increase the stock in json
                                   i.stock += stock
                                   break
                     
              # doesnt exist
              else:
                     self.products.append(Product(name=name,price=price,stock=stock,user=user,timer=timer))

       # list of products
       def list_products(self) -> list:
              '''
              display all available product in store
              list our products
              '''
              # if there is no products exist in the list
              if not self.products:
                     print('There is no products available')
              else:
                     # for giving our products in store
                     for i,j in enumerate(self.products,start=1):
                            print(f'[{i}] {j.name} - ${j.price:.2f} - stock: {j.stock}')
       # List products for adding in json 
       def save_to_json(self) -> list:
              """
              Save store products to a JSON file.
              """
              file_path = "info.json"
              data = [
                     {'name':j.name, 'price':j.price, 'stock':j.stock, 'user': j.user, 'date': j.timer}
                     for j in self.products
              ]

              with open(file_path, "w", encoding="utf-8") as f:
                     json.dump(data, f, ensure_ascii=False, indent=2)

       # find a product
       def find_products(self,name:str) -> bool:
              '''
              find a product by name
              '''
              # search
              for p in self.products:
                     if p.name.lower() == name.lower():
                            return p
              return False