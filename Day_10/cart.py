class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return f"{self.name} - ${self.price}"
class Cart:
    def __init__(self,owner):
        self.owner=owner    
        self.items=[]
    def add_item(self,product):
        self.items.append(product)
        print(f"{product.name} added to {self.owner}'s cart")
    def show_cart(self):
        print(f"{self.owner}'s cart:")
        for i in self.items:
            print(f"- {str(i)}")    
    def get_total(self):
        x=0
        for i in self.items:
            x=x+(i.price)
        print("Total: $"+str(x))             

cart = Cart("Kasi")

p1 = Product("Laptop", 999.99)
p2 = Product("Phone", 499.99)
p3 = Product("Headphones", 149.99)

cart.add_item(p1)
cart.add_item(p2)
cart.add_item(p3)

cart.show_cart()
cart.get_total()