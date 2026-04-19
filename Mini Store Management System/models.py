"""
This is for product
represent products' information in store
"""
class Product:
       # Our products name price and qunatitiy
       def __init__(self, name:str, price:float, stock:int, user:str, timer:str):
              '''
              initialize a product
              showing the information of each product in the shop
              arguments:
                     name -> str, price -> float, stock -> int
              '''
              self.name = name
              self.price = price
              self.stock = stock
              self.user = user
              self.timer = timer

              
"""
This is for cartItem
represent and holding an available item with number of purchase in the box
"""
class CartItem:
       """
       Initialize a cart item
       product -> obj, quantitiy -> int
       """
       def __init__(self,product:Product,quantity:int) -> None:
              self.product = product
              self.quantity = quantity