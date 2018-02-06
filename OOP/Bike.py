class Bike(object):
    def __init__(self, price, speed):
        self.price = price
        self.max_speed = speed
        self.miles = 0
    def ride(self):
        print ("Riding")
        self.miles +=10
        return self
    def displayInfo(self):
        print("price is ", self.price)
        print("max. speed is ", self.max_speed)
        print("total miles is ", self.miles)
    def reverse(self):
        print ("Reversing")
        self.miles -=5
        if self.miles < 0:
            self.miles =0
        return self  
        

bike1 = Bike(200, "25mph")
bike2 = Bike(300, "60mph")
bike3 = Bike(10, "5mph")

#Have the first instance ride three times, reverse once and have it displayInfo().
#Have the second instance ride twice, reverse twice and have it displayInfo(). 
#Have the third instance reverse three times and displayInfo().
#What would you do to prevent the instance from having negative miles?
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()

bike3.ride().reverse().displayInfo()