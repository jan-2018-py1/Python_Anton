'''
PART I
Create a Python class called MathDojo that has the methods add and subtract.
Have these 2 functions take at least 1 parameter.

Then create a new instance called md. It should be able to do the following task:

md.add(2).add(2,5).subtract(3,2).result
which should perform 0+2+(2+5)-(3+2) and return 4.
'''
class MathDojo(object):
    def __init__(self):
        self.total = 0
    def add(self, arg, *args):
        self.total += arg
        for i in args:
            self.total += i
        return self
    def subtract(self, arg, *args):
        for i in args:
            arg += i
        self.total -= arg    
        return self

md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).total

'''
PART II
Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with 
any number of values passed into the list. It should now be able to perform the following tasks:

md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.
'''
class MathDojo2(object):
    def __init__(self):
        self.total = 0
    def add(self, *args):
        if type(args) == int:
            self.total += args
        elif type(args) == list:
            for i in args:
                self.total += i
        return self
    def subtract(self, *args):
        if type(args) == int:
            self.total -= args
        elif type(args) == list:
            temp = 0
            for i in args:
                 temp += i
            self.total - temp  
        return self

md = MathDojo2()
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).total

'''
PART III
Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons.
'''

class MathDojo3(object):
    def __init__(self):
        self.total = 0
    def add(self, *args):
        for i in args:
            if type(i) == int:
                self.total += i
            elif type(i) == list:
                for x in i:
                    self.total += x
            elif type(i) == tuple:
                for tum in i:
                    self.total+=tum
        return self
    def subtract(self, *args):
        for arg in args:
            if type(arg) == int:
                self.total -= arg
            elif type(arg) == list:
                temp = 0
                for i in arg:
                    temp += i
                self.total -= temp      
            elif type(arg) == tuple:
                temp = 0
                for i in arg:
                    temp += i
                self.total -= temp  
        return self

md = MathDojo3()
print md.add([1], 3,4).add((3,5,7,8), [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).total