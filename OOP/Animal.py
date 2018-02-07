class Animals(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -=1
        return self
    def run(self):
        self.health -=5
        return self
    def display_health(self):
        print ("health:", self.health)
        return self

# Create instance of Animals
animal_obj = Animals("Elephant", 100)
animal_obj.walk().walk().walk().run().run().display_health()

class Dog(Animals):
    def pet(self):
        self.health +=5
        return self

dog1 = Dog("Rex", 150)
dog1.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animals):
    def fly(self):
        self.health -=10
        return self
    def display_health(self):
        print ("health:", self.health)
        print ("I am a Dragon")
        return self

animal_obj2 = Animals("Panda", 100)
animal_obj2.display_health()

dog2 = Dog("Bobic", 150)
dog2.display_health()