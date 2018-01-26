# Multiples

for i in range(2, 1001, 2):
    print(i)

for i in range(5, 1000000, 5):
    print(i)

# Sum List
a = [1, 2, 5, 10, 255, 3]

sumA = 0

for key in a:
    sumA += key

print("Sum=", sumA)

#Average List

a = [1, 2, 5, 10, 255, 3]
avrg = 0
for key in a:
    avrg += key

print(avrg/len(a))