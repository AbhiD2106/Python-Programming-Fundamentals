#strings are immutable(cant chnge)
name = "abhi7585788"

# name[0] = "M"       #can't change 

#length
#it count also space
a = len(name)
print(a)

hello = " hello world "
world = "YYHB"

print(hello.upper(),hello)
print(world.lower(),world)

print(hello.capitalize())   #first capital
print(hello.title())

print(hello.strip())        #remove unnessory space

print(hello.lstrip())        #remove unnessory left space
print(hello.rstrip())        #remove unnessory right space

#find

text = "python with fun"
print(text.find("wi"))      #o/p = 7 

#replace

print(text.replace("fun","enjoy"))      #python with enjoy

#split with ,

text1 = "apple,banana,mango"
print(text1.split(","))

#join with ,

print(",".join(['apple','banana','mango']))

text2 = "python12345"
print(text2.isalpha())      #all char is alphabate orr not
print(text2.isdigit())      #all digit or not
print(text2.isalpha())
print(text2.isspace())