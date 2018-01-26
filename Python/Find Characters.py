def findchar(list1, char1):

    result = []

    for key in list1:
        for i in key:
            if i == char1:
                result.append(key)

    print (result)

pass


word_list = ['hello','world','my','name','is','Anna']
char = 'o'

findchar(word_list, char)