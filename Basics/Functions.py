#Function Use in python3
# Simply Function working
def function_1(c='default1',y='default2'):      #Used to counter possibilty if no input given
'''Used to display if Function works'''         #Used to be Self-Examplable for what the Function is
    print('Running Function',c,y)
function_1(y="OK",c="DONE")
print(function_1.__doc__)   #Used to display the quoted line of the Function

#Function with return
def function_1(c,y):
    return c+y
x=function_1(10,20)
print(x)

a=10
def function_1(c,y):
    global a                #to enable the use of the global variable(a)
    print(a)
    a=c+y
    return a
x=function_1(10,20)
print(x)

def add(*num):              #In time when number of arguement is not known
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
