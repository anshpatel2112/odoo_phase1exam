class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, discount_percent):
        discount_amount = self.price * (discount_percent / 100)
        self.price -= discount_amount
        return self.price

class Electronics(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period

product1 = Product("Book", 500)
product2 = Electronics("Laptop", 50000, "2 years")
product3 = Product("Chair", 2000)

product1.apply_discount(10) 
product2.apply_discount(15)  
product3.apply_discount(5)   

print(f"{product1.name} final price: {product1.price}")
print(f"{product2.name} final price: {product2.price}")
print(f"{product3.name} final price: {product3.price}")