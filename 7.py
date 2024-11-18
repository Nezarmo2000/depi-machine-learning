rows = 7
cols = 7

for i in range(rows):
    for j in range(cols):
        if (j == 3 and i != 3) or (i == 3 and j != 0 and j != 6) or (i == 0 and j != 3) or (i == 6 and j != 3):
            print("*", end="")
        else:
            print(" ", end="")
    print()  
