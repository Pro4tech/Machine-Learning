v=25
name1='Pritesh'
name2='Naik'
print('Hello World',25)
print("Name",name1,sep=':',end='\n')
print(f'Hello {name1} and surname {name2}') #f'-It is used so that name1 and name2 can be accesible

print('Variable test:')
x=6
print(x)

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return fact(n-1)*n
x=fact(5)
print(x)
