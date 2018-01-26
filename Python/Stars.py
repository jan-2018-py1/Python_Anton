#Part1. Create a function called draw_stars() that takes a list of numbers and prints out *.
def draw_stars(in_list):
    for key in in_list:
        my_line = ""
        for i in range(0,key):
            my_line += "*"
        print my_line

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

#Part 2

def draw_stars2(in_list):
    for key in in_list:
        my_line = ""
        if isinstance(key, str):
            lt = key[0]
            for t in range (0, len(key)):
                my_line += lt
        else:
            for i in range(0,key):
                my_line += "*"
        print my_line.lower()

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x)