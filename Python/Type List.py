def typelist(incominglist):
    
    sum=0
    text="String: "

    if all(isinstance(key, int) for key in incominglist):
        print("The list you entered is of integer type")
        for key in incominglist:
            sum += key
        print('Sum: '+repr(sum))
    elif all(isinstance(key, str) for key in incominglist):
        print("The list you entered is of string type")
        for key in incominglist:
            text += (key+" ")
        print(text)     
    else:
        print("The list you entered is of mixed type")
        for key in incominglist:
            if(isinstance(key, str)):
                text += (key+" ")
            else: 
                sum += key
        print('Sum: '+repr(sum))
        print(text)

#    elif any(isinstance(key, int) for key in incominglist): 

    pass


mylist = ["foo", 5, 6, "loo"]
mylist2 = [4, 5, 6, 7, 8]
mylist3 = ["magical", 'unicorn']

typelist(mylist)
typelist(mylist2)
typelist(mylist3)