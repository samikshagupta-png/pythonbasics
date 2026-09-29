import random;

def rock_paper_scissors(num1,num2,bit1,bit2):
    p1=int(num1[bit1]%3)
    p2=int(num2[bit2]%3)
    if(player_one[p1]== player_two[p2]):
        print("Draw")
    elif (player_one[p1] == "Rock" and player_two[p2] == "Scissors") \
        or (player_one[p1] == "Paper" and player_two[p2] == "Rock") \
        or (player_one[p1] == "Scissors" and player_two[p2] == "Paper"):
        print("Player 1 wins 🎉")
    else:
        print("Player 2 wins 🎉")


player_one={0:'Rock',1:'Paper',2:'Scissors'}
player_two={0:'Rock',1:'Paper',2:'Scissors'}

while True:
    num1=input("player one, enter your choice: ")
    num2=input("player two,enter your choice: ")
    bit1=int(input("player 1 , enter the secret bit postion: "))
    bit2 =int(input("player 2 , enter the secret bit postion: "))
    rock_paper_scissors(num1, num2, bit1, bit2)
    ch = input("do you want to continue ? y/n: ")
    if(ch == 'n'):
        break