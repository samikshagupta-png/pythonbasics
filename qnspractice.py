# question 1
def search():
    n = int(input())
    attraction_name = {}
    for _ in range(n):
        line = input().strip()
        name,rating = line.rsplit(' ',1)
        attraction_name[name] = rating
    print(attraction_name)
    search_result = input().strip()
    if search_result in attraction_name:
        print(attraction_name[search_result])
    else:
        print(-1)

#question 2
def landmark_search():
    N = int(input().strip())
    landmark =input().strip().split()
    serach_land = input().strip()
    index=-1
    for i in range(len(landmark)):
        if landmark[i]== serach_land:
            index=i
            break

def second_max():
    n = list(map(int ,input().split()))
    r=n.sort(reverse=True)
    print(n[1])

def floor_movement():
    n = list(map(int,input() .split()))
    move =sum(n)
    print(move)

def sum_total():
    n = list(map(int , input().split()))
    score= sum(n)
    print(score)

def patterns():
    id1,id2 = input().split()
    if len(id1) != len(id2):
        print(False)
        return
def record():
    n = list(map(int,input("enter no btw 0-255 : ").split()))
    total_sum =0
    for x in n:
        if 0<=x<=31:
            total_sum +=0
        if 32<=x<=63:
            total_sum +=1
        
        if 64<=x<=95:
            total_sum += 2
        if 96 <=x<= 127:
            total_sum += 3
        if 128<=x<= 159:
            total_sum+=4
        if 160 <= x <= 191:
            total_sum+=5
        if 192<= x <= 223:
            total_sum+=6
        if 224<= x<= 255:
            total_sum +=7
    print(total_sum)

def remove_matches():
    str1 = input().split()
    a = list(str1[0])
    b = list(str1[1])
    for ch in a[:]:
        if ch in b :
            b.remove(ch)
            a.remove(ch)
    print(len(a)+len(b))


            
# remove_matches()
# record()
# sum_total()
# floor_movement()
# second_max()
# landmark_search()
# search()