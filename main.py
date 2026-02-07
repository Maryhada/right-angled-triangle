#Take input
print("Half Pyramid Pattern of the Stars (*):")
n = int(input("enter the number of rows: "))
#outer loop to handle number of ros
for i in range(n):
    #inner loop to handle number of columns
    for j in range(i+1):
        #display result
        print("* ", end="")
    print()    