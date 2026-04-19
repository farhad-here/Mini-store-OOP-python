# import section
from models import CartItem
from store import Store
import json
# class
class Cart:
       '''
       It is for shopping cart.
       '''
       def __init__(self):
              self.items = []
       # adding product into cart
       def add_to_cart(self, product: Store, quantity: int) -> bool:
              """
              Add product to cart if stock is sufficient.
              """
              # quantitiy should not be more than storage
              if quantity > product.stock:
                     return False
              else:
                     product.stock -= quantity
              for item in self.items:
                     if item.product.name == product.name:
                            item.quantity += quantity
                            return True

              self.items.append(CartItem(product, quantity))
              return True
       # remove from cart
       def remove_from_cart(self, product_name: str) -> None:
              """
              Remove product from cart and restore stock.
              """
              for item in self.items:
                     if item.product.name.lower() == product_name.lower():
                            item.product.stock += item.quantity
                            self.items.remove(item)
                            return
       # what customer want to purchase
       def view_cart(self) -> None:
              """
              Display cart contents.
              """
              print("🛒 Your cart:")
              for item in self.items:
                     subtotal = item.quantity * item.product.price
                     print(f"- {item.product.name} x{item.quantity} - ${subtotal:.2f}")
                     print(f"💰 Total: ${self.total_price():.2f}")
       # the sum of the price
       def total_price(self) -> float:
              """
              Calculate total price of the cart.
              """
              return sum(item.quantity * item.product.price for item in self.items)
       # check out
       def checkout(self) -> None:
              # final check 
              """
              Final checkout and clear cart.
              """
              print("🧾 Final Checkout:")
              self.view_cart()
              self.items.clear()
              print("🎉 Thank you for shopping with us!")
       def add_customer_shop_json(self,customerName,customerTim):
              # json
              '''
              for adding data into json for customer
              '''
              # path for json file
              file_path = "customerHistory.json"
              with open(file_path,'r',encoding='utf-8') as fs:
                     js_data = json.load(fs)
              data = [
                     {'name':j.product.name, 'subtotal':float(f'{(j.quantity * j.product.price):.2f}'), "Total":float(f'{self.total_price():.2f}'),'quantity':j.quantity, 'user': customerName, 'date': customerTim}
                     for j in self.items
              ]
              for i in js_data:
                     data.append(i)
              # write
              with open(file_path, "w", encoding="utf-8") as f:
                     json.dump(data, f, ensure_ascii=False, indent=2)