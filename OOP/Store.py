'''
Now, let's build a store to contain our products by making a store class and putting our products into an array.

Store class:
Attributes:

• products: an array of products objects

• location: store address

• owner: store owner's name

Methods:

• add_product: add a product to the store's product list

• remove_product: should remove a product according to the product name

• inventory: print relevant information about each product in the store

You should be able to test your classes by instantiating new objects of each class and using the outlined methods to demonstrate that they work.
'''

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    def add_product(self, product):
        self.products.append(product)
        return self
    def remove_product(self, product):
        self.products.remove(product)
        return self
    def inventory(self):
        print ("Store location: ", self.location)
        print ("Owner ", self.owner)
        print ("Store inventory: ", self.products)
        
store043 = Store(["MC54", "MC57", "Zebra TC75", "MC007"], "Owings Mills", "Anton")

store043.add_product("Intermec").remove_product("MC57").inventory()
