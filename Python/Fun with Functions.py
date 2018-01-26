#Odd/Even:

def odd_even():
    for i in range(1,2001):
        if i%2 == 0:
            print "Number is ", i, "This is an even number"
        else:
            print "Number is ", i, "This is an odd number"

#odd_even()

def multiply(incoming_list, value):
    result=[]
    for key in incoming_list:
        result.append(key*value)
    return result

a = [2,4,10,16]
b = multiply(a, 5)
print b

#Hacker Challenge
def layered_multiples(arr):
  new_array = []
  for i in range(0, len(arr)):
    l = []
    for j in range(0, arr[i]):
        l.append(1)
    new_array.append(l)
  return new_array

x = layered_multiples(multiply([2,4,5],3))
print x