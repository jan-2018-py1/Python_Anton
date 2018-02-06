class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price>10000:
            self.tax = "15%"
        else:
            self.tax = "12%"
        self.display_all()
    def display_all(self):
        print ("Price: ", self.price)
        print ("Speed: ", self.price)
        print ("Fuel: ", self.price)
        print ("Mileage: ", self.price)
        print ("Tax: ", self.price)

ford = Car(2000, "35mph", "Full", "15mpg")
ford_01 = Car(20000, "35mph", "Full", "15mpg")
