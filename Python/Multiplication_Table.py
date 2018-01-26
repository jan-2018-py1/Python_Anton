flag = True

for i in range(1, 13):
    line = ""
    for k in range(1, 13):
        num= i*k
        if flag:
            line+=" " + "x"
            flag = False
        else: line+=" " + str(num)
    print(line)

#tested on Python3 