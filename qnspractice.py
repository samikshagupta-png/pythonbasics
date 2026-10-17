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

    


# sum_total()
# floor_movement()
# second_max()
# landmark_search()
# search()