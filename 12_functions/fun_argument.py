def sum(a,b):
    c = a+b
    return c

o1 = sum(2,4)
print(o1)

#default args

def sum_default(a,b,plus=0):
    c = a+b+plus
    print(c)

sum_default(3,5,2)


#keyword args

def keyw(name,age):
    print(name,"=",age)

keyw(name="abhi",age=21)


