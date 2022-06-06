"""
For any class, a user should be able to use its subclasses indistiguishably without
noticing or compromising the expected behaviour at runtime
A superclass object should be replaceable by the subclass object without breaking/
changing the functionality
Child class must be substitutable for parent class
"""

from abc import ABC, abstractmethod

# EXAMPLE 1 WITHOUT LSP
class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total



class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order, security_code):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing paypal payment type")
        print(f"Using email address: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor()
processor.pay(order, "hi@arjancodes.com")

"""
Our superclass expects 2 arguements, order and security code. Paypal payments 
don't use security codes but instead use email addresses. Our code Paypal payment
processor is however taking the security code then forcing it to be used as email
therefore defying the Liskov's substitution principle. 
"""

# EXAMPLE 2 WITH LSP
class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code
    
    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address):
        self.email_address = email_address

    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor("hi@arjancodes.com")
processor.pay(order)

"""
Second example is in line with LSP as we don't have to change what 
parameters represent so as to fit our particular use case. Parameter definitions
are now universal
"""