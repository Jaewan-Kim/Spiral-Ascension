userInput = int(input('Please enter a number(the program will crash if you dont: '))

right = 1;
down = 2;
left = 3;
up = 4;

direction = right;

current_number = 1;

vec = []


def left_exists(userin , current) :
    if (current-1) % userin == 0:
        return False;
    else:
        return True;


def right_exists(userin , current) :
    if current % userin == 0:
        return False;
    else:
        return True;


def up_exists(userin , current) :
    if (current-1) % userin == 0:
        return False;
    else:
        return True;


def down_exists(userin , current) :
    if current <= userin:
        return False;
    else:
        return True;


while current_number < userInput* userInput:
    vec.insert(0,7);

for int in vec:
    print(int)