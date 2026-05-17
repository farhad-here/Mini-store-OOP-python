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
              self.load_from_json()
       def load_from_json(self):
              file_path = "info.json"
              try:
                     with open(file_path, 'r', encoding='utf-8') as fs:
                            js_data = json.load(fs)
              except (FileNotFoundError, json.JSONDecodeError):
                     js_data = []

              self.products = [
                     Product(name=item['name'],
                            price=item['price'],
                            stock=item['stock'])
                     for item in js_data
              ]

       
       # method add product -> name price stock
       def add_product(self,name:str,price:float,stock:int,user:str,timestamp:str):
              '''
              add new product to the store
              if product exist so just update the price and stock
              '''
              # find about if product exist or not (searching by the name)
              exist_product = self.find_products(name=name)
              if exist_product:
                     exist_product.price = price
                     exist_product.stock += stock
              else:
                     self.products.append(Product(name=name, price=price, stock=stock))
                     


                        
             

       # list of products
       def list_products(self) -> list:
              if not self.products:
                     print("There is no products available")
                     return

              for i, product in enumerate(self.products, start=1):
                     print(f"[{i}] {product.name} - ${product.price:.2f} - stock: {product.stock}")

       # List products for adding in json 
       def save_to_json(self):
              file_path = "info.json"

              data = [
                     {
                     "name": p.name,
                     "price": p.price,
                     "stock": p.stock
                     }
                     for p in self.products
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
