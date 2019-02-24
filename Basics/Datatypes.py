a,b=7,3    #Variable In&Assign
print("Addition",a+b)
print("Subtraction"a-b,sep=':')
print("Multiplication"a*b,sep=':')
print("Division Float"a/b,sep=':')
print("Division Int"a//b,sep=':')
print("Modulo"a%b,sep=':')
print("Expo"a**b,sep=':')

#String Implementaion
s1='Pritesh'
s2='Jagnath'
print(s1+s2)    #Concatination
print(s1*3)     #Mutliple output
print(s1[0])    #Array implementaion
print(s2[-1])   #Array implementaion Using -ve index
print(s1[1:4])  #Array Range:Splicing Rule
print(len(s1))  #String Lenth

#List Implementaion
n1=[2,4,5,7,9,10]       #List implementaion
print(n1[3])
print(n1[1:3])          #List Accesing using range
print(n1[-3])           #List Accesing using -ve Index
n1.append(12)           #List Append Property-Single element
print(n1)
n1.extend([13,14])      #List extend Property-Multi element
n1.extend('stop')      #List extend Property-Multi element
print(n1)
n1.insert(1,52)         #List insert Property-Single element(Index,element)
print(n1)
print(n1.index('o'))   #List Index Property-Find element
del(n1[5])              #List deletion Property- deletion Single element
del(n1[:2])             #List deletion Property- deletion Multiple element using Splicing
print(n1)
n1.sort()               #List sort
print(n1)

#Function Use in Python3
# Simply Function working
def function_1(c='default1',y='default2'):      #Used to counter possibilty if no input given
    #Used to display if Function works
    print('Running Function',c,y)
function_1(y="OK",c="DONE")
print(function_1.__doc__)   #Used to display the quoted line of the Function

#Function with return
def function_1(c,y):
    return c+y
x=function_1(10,20)
print(x)

#Functions with Global Variables
a=10
def function_1(c,y):
    global a                #to enable the use of the global variable(a)
    print(a)
    a=c+y
    return a
x=function_1(10,20)
print(x)

def add(*num):              #In times when number of arguement is not known
    sum=0
    for i in num:
        sum=sum+i
    return sum
x=add(1,2,3)                #nums here is something called as a tuple
print(x)

#The working of Tuple datastructure
tuple=(1,'hello',3.5,[2,5,6],3,4,3)
print(tuple)
print(tuple[-4][2])         #to Access ineer lists in a tuple
print(3.5 in tuple)         #to check if an element exists in a Tuple
print(tuple.count(3))       #to display the number of times an element exists
print(tuple.index(3))       #to display the index of 1st occurance in a Tuple

#Dictonaries datastructure
dict={'a':'apple','b':'ball','1':'test','nest':{1:'nested',2:'nest'}}
print(dict['b'])                           #to Access value of a given key
print(dict.get('1'))                       #to Access value of a key by Function
dict['b']='bat'                            #to change value of a key
print(dict.get('b'))
print(dict['nest'])

#Class Implementaion
class  C1:
    """Property Of Car"""
    #pass                        #It aloows the program to work when condition is not given
    fuel='full'

    def __init__(self,a,b):         #Constructor Defination init is a in-built Function
        print("This prints car speed")
        self.max_speed=a
        self.time=b               #"__"(2x_) allows for securing the unauthorised usage
    def calc(self):
        distance=self.max_speed * self.time
        return distance
class C2(C1):
    pass
    print("Class 2")

obj1=C2(10,5)                       #Instant creation
print("start")
print(obj1.calc())                  #Instant Function call
print(obj1.__doc__)
obj2=C1(25,5)
print(obj2.max_speed)
print(C1.fuel)                      #Accesing using class Name
print(type(obj1))
