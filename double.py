import string;
import random;
symbols=[]
symbols=list(string.ascii_letters)
card1 =[None]*5

card2 = [None]*5
pos1 = random.randint(0,4)
pos2 = random.randint(0,4)
# print(pos1)
# print(pos2)
samesymbol = random.choice(symbols)
symbols.remove(samesymbol)

# Place common symbol correctly
card1[pos1] = samesymbol
card2[pos2] = samesymbol

# If positions differ, fill swapped spots
if pos1 != pos2:
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
for i in range(5):
    if card1[i] is None:
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        card1[i] = alphabet1
    if card2[i] is None:
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        card2[i] = alphabet2

print(card1)
print(card2)
ch = input("spot the similar symbol :")
if(ch == samesymbol):
    print("Right")
else:
    print("wrong The correct symbol was:", samesymbol)
