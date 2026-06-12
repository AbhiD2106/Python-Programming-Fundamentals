a = {33,44,22,55,33,22}
print(a, type(a))

#duplicate not allowed
#unordered
# print(a[3])  # sets are unordered and unindexed

a.add(77)
print(a)
a.remove(33)
print(a)
a.discard(323)  # if element not found it will not give error
print(a)
a.pop()
print(a)
a.clear()
print(a)