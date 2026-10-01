
import random;
# guess your parter match by name 
willing=True
while willing:
    name = input("enter your name: ")
    print("welcome " , name)
    name = input("enter your parter name: ")
    n = random.randint(0,101)
    if 0<=n<=20:
        print("The percentage of your love is : " ,n ,'%',"\nfriendzone alert: better start looking for someone else!")
    elif 20<n<40:
        print("The percentage of your love is : " ,n ,'%',"\npoor match ! ... you two are like oil and water ")
    elif 40<=n<=50:
        print("The percentage of your love is : " ,n ,'%',"\njust okay .. maybe a casual coffee, but don't plan the wedding ")
    elif 50<n<60:
        print("The percentage of your love is : " ,n ,'%',"\nsparks are there ! A liitle efforts could turn this into something sweet..")
    elif 60<=n<=70:
        print("The percentage of your love is : " ,n ,'%',"\ncute couple material ...")
    elif 70<=n<=80:
        print("The percentage of your love is : " ,n ,'%',"\nStrong connections ! things are getting warm in there")
    elif 80<n<=90:
        print("The percentage of your love is : " ,n ,'%',"\nhead over heels!  pure chemistry  & fireworks")
    else:
        print("The percentage of your love is : " ,n ,'%',"\nwin the match , soulmates")

    will=input('are you want to continue ? y (yes) /n (no)')
    if will == 'n':
        willing=False


