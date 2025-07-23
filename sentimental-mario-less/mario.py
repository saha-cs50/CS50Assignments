from cs50 import get_int

# get user input
while True:
    height = get_int("Enter a positive integer: ")
    if height > 0 and height < 9:
        break

i = 0
j = 0
k = 0
tempheight = height - 1

while i < height:
    k = 0
    # controls spaces
    while k < tempheight:
        print(" ", end="")
        k = k + 1
    # controls hashes
    while j < i + 1:
        print("#", end="")
        j = j + 1
    print()
    i = i + 1
    j = 0
    tempheight = tempheight - 1