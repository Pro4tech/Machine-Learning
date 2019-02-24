#Basic Loops
a=14
#If-Else [elif-Combi of both]
if a>0:
    print("Positive")
elif a==0:
    print("Zero")
else:
    print("Negative")

if a<6 and a>4:
    print("Num is 5")
elif a<4:
    print("Below the range")
else:
    print("Above the range")

c=[1,2,3,4,52,7,9,8,5,2]

if 51 in c:
    print("element present")
else:
    print("Absent")

a=0
#While Loops
while a<9:
    print(a)
    a+=1
while True:
    print(a)

#For loops using Range
for i in range(10):
    if i==3:
        print('break')
        break
for j in range(5):
    if j==2:
        print("continue")
        continue

for i in range(10):         #range syntax:range(start,stop,step)
    print(i)
for j in range(5,10):
    print(j)
for k in range(5,20,5):
    print(k)

c=['jon','dan','rob','mike']    #For in List implementaion
for Name in c:
    print(Name)

#Fibonacci Seies and Reversal
def fibo(n):
    if(n==0):
            return 0
    if(n==1):
        return 1        
    else:
        return fibo(n-1)+fibo(n-2)
n=input("Enter the Inputs:")
for i in range(n):
    x=fibo(i)
    print(x)

print("Reversal:")
a=input("Enter the Input:")
b=0
print("Input Number:"+str(a))
while a>0:
    x=a%10
    b=b*10+x
    a=a/10
print("Reversed Number:"+str(b))

#Exceptions
import sys              #Needed For Exceptions
relist=[1,0,5,'a']

for i in relist:
    try:
        print('The Element is',i)
        result=10/int(i)
        print('Results:'+str(result))
    except:
        print("He got an Error")
