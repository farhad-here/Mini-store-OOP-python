# 🛍️ Mini Store Management System (Console Application)

A simple console-based store simulation written in Python, designed to practice **OOP**, **modular coding**, and **CLI interaction**.  
This project includes product management for a store manager and shopping features for customers.

---

## 🚀 Features

### 👨‍💼 Store Manager
- Add new products with name, price, and stock
- View all products in the store
- Prevent adding invalid data
- Secure login system (`admin / 1234` by default)

### 🧑‍💻 Customer
- View all available products
- Add items to shopping cart
- Prevent adding more items than available stock
- Remove items from cart
- View cart contents at any time
- Checkout with final invoice

### 🧾 Additional Behaviors
- Automatic stock updates after adding to cart  
- Input validation for all user choices  
- Clear and readable console UI  
- Fully modular code following clean architecture principles  

---

## 🧱 Project Structure (Classes)

### `Product`
Represents each product in the store.
- `name: str`
- `price: float`
- `stock: int`

### `Store`
Manages all products.
- `products: list[Product]`
- `add_product(name, price, stock)`
- `list_products()`
- `find_product(name)`

### `CartItem`
Represents a single item in the shopping cart.
- `product: Product`
- `quantity: int`

### `Cart`
Handles cart operations.
- `items: list[CartItem]`
- `add_to_cart(product, quantity)`
- `remove_from_cart(product_name)`
- `view_cart()`
- `total_price()`

---

## 📸 Sample Output
================================= 🛍️ MINI STORE MANAGEMENT SYSTEM
```bash
👋 Welcome! Please select your role:

Store Manager
Customer
Exit Program
Enter choice: 1

🔐 Store Manager Login
Username: admin

Password: 1234

✅ Login successful! Welcome, Manager.

📦 Add Products
Enter product name (or ‘done’ to finish): Laptop

Enter product price: 1200

Enter product stock quantity: 5

✅ Product added: Laptop - $1200.00 (Stock: 5)

```

(Full output available in your program.)

---

## ▶️ How to Run

1. Make sure you have **Python 3.8+** installed.
2. Clone this project:
```bash
git clone https://github.com/<your-username>/<repo-name>.git
```
3.Run the main file:
```bash
python main.py
```
## 🧠 Skills Practiced
- Object-Oriented Programming (OOP)
- Class design and interaction
- CLI-based user interface
- Input validation
- Clean and modular code organization
- Docstrings & Type Annotations
### ⭐ Optional Enhancements (Extra Features)
- Product categories✔️
- User authentication system for multiple customers✔️
- Saving/loading store data using JSON✔️
- Logging purchase history per customer✔️
- Colorful CLI output with colorama❌

### 📌 Notes
This project is designed as a practice assignment to simulate a real store environment using only Python console programming and clean OOP structure.


