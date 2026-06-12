
# a = input("enter number A = ")
# print(a + 3)

# ERROR for type casting

#   File "e:\python\python\05_userinput\add.py", line 4, in <module>
#     print(a + 3)
#           ~~^~~
# TypeError: can only concatenate str (not "int") to str
# solve : a = int(input("enter number A = "))     

a = int(input("enter number A = "))
b = int(input("enter number B = "))

print(a + 3)
print(a + b)