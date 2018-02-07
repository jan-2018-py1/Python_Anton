'''
The owner of a store wants a program to track products. Create a product class to fill the following requirements.

Product Class:
Attributes:

• Price

• Item Name

• Weight

• Brand

• Status: default "for sale"

Methods:

• Sell: changes status to "sold"

• Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax

• Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0.
If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.

• Display Info: show all product details.

Every method that doesn't have to return something should return self so methods can be chained.
'''

class Product(object):
    def __init__(self, price, name, weight, brand, tax, status="for sale"):
        self.price = price
        self.item_name = name
        self.weight = weight
        self.brand = brand
        self.status = status
        self.tax = tax
    def display_info(self):
        print("Price: ", self.price)
        print("Title: ", self.item_name)
        print("Weight: ", self.weight)
        print("Brand: ", self.brand)
        print("Status", self.status)   
        print("Total price: ", self.finalPrice())
        return self
    def sold(self):
        self.status = "Sold!"
        return self
    def finalPrice(self):
        final_price = self.price + (self.price*self.tax)
        return final_price
    def returns(self, reason):
        if reason == "defective":
            self.status = "Defective"
            self.price=0
        elif reason == "in box":
            self.status = "for Sale"
        else:
            self.status = "Used"
            self.price= self.price - (self.price * 0.20)
        return self

shoes = Product(25.55, "MC Fly", 55, "MC", 0.06)
        
shoes.sold().display_info()
