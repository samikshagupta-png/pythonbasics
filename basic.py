# # # fibonacci series
# # n=int(input("enter number:"))
# # a=0
# # b=1
# # count=0
# # if n==1:
# #     print(a)
# # else:
   
# #     while count< n:
# #         print(a, end=" ")
# #         nth=a+b
# #         a=b
# #         b=nth
# #         count=count+1
# # n=int(input("enter terms:"))
# # sum=0
# # while n>0 :
# #     term=n%10
# #     sum+=term
# #     n=n//10


# # print("sum of a digit :",sum)
# # pugrint(10//3)


# # for i in range (0,n):
# #     print("* " * (n-i))

# # for i in range(0,n):
# #     print(" " * (n-i) + ("* " *i) )
#     # print( ("* " *i))
# # def gcd(a,b):
# #     while b!=0:
# #         a,b=b,a%b
# #     return a
# # print(gcd(48,18))
    
# # def main():
# #     gcd(48,18)

# # if "__main__" =="__name__":
# #     main()

# # n= int (input("enter a number:"))
# # r = int(input("Enter the value of r:"))
# # sum =0

# # for i in range (1,n):
# #     if n%i == 0:
# #         sum = sum + i
        
# # if sum == n:
# #     print("perfect number")
# # else :
# #     print("not")           
# def factorial(p):
#     fact=1
#     for i in range(1,p+1):
#         fact*=i
#     return fact
# # def npr(n,r):
# #     x=factorial(n)//factorial(n-r)
# #     return x
# def npr(n, r):
#     if r > n:
#         return "Invalid: r cannot be greater than n"
#     return factorial(n) // (factorial(n-r) * factorial(r))

# def main():
#     result = npr(1,2)
#     print("nCr=" , result)
# if __name__ == "__main__" :
#     main()
        
# for i in range(1,5):
#     print('* '* i)

# n = int(input("enter a number: "))
# for i  in range (1,n):
#     if (n % i==0) :
#         print(i)

# line = input("enter line :")
# rev = line[-1:0]
# print(rev)
# physics=float(input("enter your marks here: "))
# maths= float(input("enter your marks here: "))
# chemistry=float(input("enter your marks here: "))
# avg = (physics+maths+chemistry )/ 3
# print(avg)

# #  acc of a moving body
# u=0
# v=10
# t=20
# acc= (v-u)/ t
# print (acc)

# # richer magnitude
# rm = float(input("enter richer magnitude: "))
# if (1.0 < rm < 2.9):
#     print("Microearthquakes not felt or rarely felt")
# elif (4.0 < rm < 5.9):
#     print("Damage done to weak buildings")
# elif(7.0 < rm < 8.9):
#     print("Causes damage to most buildings")
# else:
#     print(" Causes unbelievable damage")

# # check leap year or not
# year = int(input("enter yaer: "))
# if ( year % 400==0 and year % 100==0):
#     print("leap year")
# elif(year %4 == 0 and year % 100 !=0):
#     print("leap year")
# else :
#     print("not a leap year")

# # factorial of a number
# def fact(n):
#     if (n==1 or n==0):
#         print("factorial is 1")
#     else:
#          return n *fact(n-1)
        

# print("factorial is " , fact(5))

# # 'area of pentagon
# base= float(input("enter base:"))
# height = float(input("enter height :"))
# #  area of a regular pentagon
# area= 5/2 *base *height
# print ("the area is ",float(area))

# # convert centigrade into fahrenheit
# centigrade = float(input("enter temperature in Centigrade"))
# fahrenheit = (centigrade * 9/5) + 32
# print(centigrade," centigrade is " ,fahrenheit,"fahrenheit")


# n=int(input("enter number: "))
# m=int(input("enter 2nd number: "))

# for i in range(n,m+1):
#     if i >1 :
#         for j in range(2,i):
#             if(i % j==0):
#                 break
#         else:
#             5
#             print(i)
# n = int(input("enter number:"))
# order=len(str(n))
# temp = n
# sum =0
# while temp >0:
#     digit = temp % 10
#     exp = digit ** order
#     sum= sum + exp 
#     temp = temp // 10
# if sum == n :
#     print("it is armstrong")
# else :
#     print("not a armstrong ")

# word = input("enter word:")
# rev = word[::-1]
# if (word == rev):
#     print("plaindrome")
# else:
#     print("error")

# n=5
# for i in range (0,5):
#     print("* " * i)



