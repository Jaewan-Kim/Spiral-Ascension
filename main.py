userInput = int(input('Enter a number: '));


Matrix = [[0 for x in range(userInput)] for y in range(userInput)]


current_number = 0
hmax = userInput-1
vmax = userInput-1
hindex = 0
vindex = 0
hmin = 0
vmin = 1

squared = userInput * userInput
right = 1
down = 2
up = 3
left = 4
direction = right

while current_number < squared:
    current_number += 1
    Matrix[vindex][hindex] = current_number
    print(Matrix)
    if direction==right :
        if hindex == hmax:
            vindex +=1
            hmax -=1
            direction = down
        else:
            hindex +=1
    elif direction==down:
        if vindex == vmax:
            vmax -=1
            hindex -=1
            direction = left

        else:
            vindex+=1
    elif direction == left:
        if hindex == hmin:
            hmin += 1
            vindex -= 1
            direction = up
        else:
            hindex -=1
    elif direction == up:
        if vindex == vmin:
            vmin +=1
            hindex +=1
            direction= right
        else:
            vindex-=1

for x in range(0,userInput):
    print(Matrix[x])