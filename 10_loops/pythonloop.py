mylist = ["orders","products","customers"]

for i in range(1,100):
    print(i)


for i in mylist:
    print(i)


#if combines with loops
print("\n")
for i in mylist:
    if i.lower() == "products":
        print("table order")
    else:
        print("no in order")


print("\n")
for a in mylist:
    print(a)
    for x in a:
        print(x)


#while and break

print("\n")
x = 1
while 1==1:
    print("hello")
    x = x + 1

    if x > 10:
        break