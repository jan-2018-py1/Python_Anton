my_dic = {
    "name":"Anton", 
    "age":"36", 
    "country of birth":"Belarus", 
    "favorite language":"JS"
}

def print_data(dictr):
    for key, value in dictr.iteritems():
        print 'My', key, 'is', value

print_data(my_dic)