"""
A class should have one and only one job/responsibility. If a class
has more than one responsibilty, it becfomes coupled and changing on responsbility,
leads to changing another responsibility
"""
# Example1 without SRP

# class  User:
#     def __init__(self, name: str):
#         self.name = name
#     
#     def get_name(self) -> str:
#         pass
# 
#     def save(self, user):
#         pass

"""
The class above handles both user properties and user DB Managaement.
If we make changes to the dB management functions, we'll have to make changes to DB
properties too
"""

# Example with SRP

# class User:
#     def __init__(self, name: str):
#             self.name = name
#     
#     def get_name(self):
#         pass
# 
# 
# class UserDB:
#     def get_user(self, id) -> User:
#         pass
# 
#     def save(self, user: User):
#         pass

"""
User properties and user database management are now decoupled therefore making
it easier to make changes if we desire to 
"""

## Example2 without SRP

# class Order:
# 
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = "open"
# 
#     def add_item(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
# 
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total
# 
#     def pay(self, payment_type, security_code):
#         if payment_type == "debit":
#             print("Processing debit payment type")
#             print(f"Verifying security code: {security_code}")
#             self.status = "paid"
#         elif payment_type == "credit":
#             print("Processing credit payment type")
#             print(f"Verifying security code: {security_code}")
#             self.status = "paid"
#         else:
#             raise Exception(f"Unknown payment type: {payment_type}")
# 
# order = Order()
# order.add_item("Keyboard", 1, 50)
# order.add_item("SSD", 1, 150)
# order.add_item("USB cable", 2, 5)
# 
# print(order.total_price())
# order.pay("debit", "0372846")
# 
## EXAMPLE2 with SRP
# class Order:
# 
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = "open"
# 
#     def add_item(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
# 
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total
# 
# class PaymentProcessor:
#     def pay_debit(self, order, security_code):
#         print("Processing debit payment type")
#         print(f"Verifying security code: {security_code}")
#         order.status = "paid"
# 
#     def pay_credit(self, order, security_code):
#         print("Processing credit payment type")
#         print(f"Verifying security code: {security_code}")
#         order.status = "paid"
# 
# 
# order = Order()
# order.add_item("Keyboard", 1, 50)
# order.add_item("SSD", 1, 150)
# order.add_item("USB cable", 2, 5)
# 
# print(order.total_price())
# processor = PaymentProcessor()
# processor.pay_debit(order, "0372846")