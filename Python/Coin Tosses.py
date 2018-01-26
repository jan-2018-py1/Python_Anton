from random import randint

def coin_tosses():
    head, eagle = 0, 0
    for i in range(1,5001):
        coinside = randint(1, 2)
        if i!=5000:
            if coinside == 1:
                head+=1
                print "Attempt #",i,": Throwing a coin... It's a head! ... Got ", head, " head(s) so far and ", eagle, " tail(s) so far"
            else:
                eagle+=1
                print "Attempt #",i,": Throwing a coin... It's a tail! ... Got ", head, " head(s) so far and ", eagle, " tail(s) so far"
        else:
            if  coinside == 1:
                head+=1
                print "Attempt #",i,": Throwing a coin... It's a head! ... Got ", head, " head(s) so far and ", eagle, " tail(s) so far"
            else: 
                eagle+=1
                print "Attempt #",i,": Throwing a coin... It's a tail! ... Got ", head, " head(s) so far and ", eagle, " tail(s) so far"
    print "Ending the program, thank you!"

coin_tosses()