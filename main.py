# import section
from store import Store
from cart import Cart
from login import managerLogin
import time

# for manager(admin portal)
def manager_portal(store: Store) -> None:
    print("🔐 Store Manager Login")
    # admin login
    if not managerLogin():
        print("❌ Login failed!")
        return

    print("✅ Login successful!")
    print('--------------------------------\n📦 Add Products\n--------------------------------')

    # admin add products
    while True:
        # name, price and quantitiy of products
        name = input("Enter product name (or 'done'): ")
        if name.lower() == "done":
            break
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        # user and time of adding product for admin
        user = 'admin'
        t_date = time.strftime('%D %H:%M')
        store.add_product(name, price, stock, user, t_date)
        store.save_to_json()
        print(f'✅ Product added: {name} - ${price} (Stock: {stock})')



# for customer
def customer_portal(store: Store) -> None:
    # class Cart
    cart = Cart()
    # customer name and date of shopping
    # customer name
    user_customer = input("Enter YourName: ")
    while True:
        # CLI for customer title
        print("\n🛍️ CUSTOMER PORTAL")
       
        print(f'Hello, dear {user_customer}')
        # list products
        store.list_products()
        # customer CLI
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Return to main Menu")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            product = store.find_products(name)
            if not product:
                print("❌ Product not found.")
            elif not cart.add_to_cart(product, quantity):
                print("❌ Not enough stock.")
            else:
                print("✅ Added to cart.")
        
        elif choice == "2":
            name = input("Enter product name to remove: ")
            cart.remove_from_cart(name)
        # see what customer purchase
        elif choice == "3":
            cart.view_cart()
        # checkout
        elif choice == "4":
            # date the customer bought something
            t_date_customer = time.strftime('%D %H:%M')
            # json
            cart.add_customer_shop_json(user_customer,t_date_customer)
            # checkout
            cart.checkout()
            break

        elif choice == "5":
            break


def main() -> None:
    store = Store()

    while True:
        print("\n🛍️ MINI STORE MANAGEMENT SYSTEM")
        print("1. Store Manager")
        print("2. Customer")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager_portal(store)
        elif choice == "2":
            customer_portal(store)
        elif choice == "3":
            print("👋 Goodbye!")
            break


if __name__ == "__main__":
    main()
