import math
def sqrtm(num):
    return math.sqrt(num).is_integer()


for i in range(100, 1001):
    for p in range(100, i):
        if i % p == 0:
            break
    else:
        print(i)


print(sqrtm(3))


# tested in Python3; the assignment is not completed;  just for testing purpose 