#bubble sort
def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j] >a[j+1]):
                tmp = a[j]
                a[j]=a[j+1]
                a[j+1]= tmp
a=[5,1,5,2,8]
bubble(a)
#print array
# for i in a:
#     print(i)

#linear search
def linear_search(n,x):
    element=[]
    for i in range(1,1001):
        element.append(i)
    
    for i in element:
        if i==x:
            print("target found ", i)
            
        
        
    
# linear_search(1001,50)

#binary search
def binary_search(a,x):
    first_pos=0
    last_pos =len(a)-1
    flag=0
    count=0
    while(first_pos<=last_pos and flag ==0):
        mid=(first_pos+last_pos)//2
        count+=1
        if(x==a[mid]):
            flag=1
            print("element is at  poisition" , mid)
            print("the no of iteration", count)
            return
        else:
            if x<a[mid]:
                last_pos=mid-1
            else:
                first_pos=mid+1
    print("element not found")
        
a=[]
for i in range(1,50):
    a.append(i)
binary_search(a,40)  