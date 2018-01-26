from random import randint

def generator():
    for i in range(0,10):
        score = randint(60, 100)
        if score<70:
            print("Score:", score, " Grade - D")
        elif score<80:
            print("Score:", score, " Grade - C")
        elif score<90:
            print("Score:", score, " Grade - B")
        elif score<101:
            print("Score:", score, " Grade - A")
        
generator()