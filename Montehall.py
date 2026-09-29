import random;
doors = [0]*3
goatdoor = [0]*2
swap =0
dont_swap =0
x= random.randint(0,2)
doors[x]="BMW"
for i in range (0,3):
    if(i==x):
        continue
    else:
        doors[i] ="goat"
        goatdoor.append(i)
choice = int(input("enter your choice: "))
door_open = random.choice(goatdoor)
while(door_open==choice):
    door_open=random.choice(goatdoor)
ch= input('do you want to swap  ? y/n ')
if(ch == 'y'):
    if(doors[choice] == 'goat'):
        print("player wins 🎉")
        swap=swap+1
    else:
        print("player lost ")

else:
    if(doors[choice] =='goat'):
        print("player lost")
    else:
        print("player wins ! 🎉")
        dont_swap=dont_swap+1
print( "no of swap" , swap)
print("no of don't swap" ,dont_swap)

