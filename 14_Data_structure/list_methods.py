students = ["abhi","dhruvi","kirtan","om","kuldeep"]
marks = [22,44,22,32,42,12]
marks_ex = [33,22,66,34]
mixed = [34,"hello",False ,3.4]

# append() = add elements in list
marks.append(32)
print("append:", marks)

# remove last element
marks.pop()
print("pop:", marks)

# insert(index,data)
marks.insert(3,77)
print("insert:", marks)

# combine two lists
marks.extend(marks_ex)
print("extend:", marks)

# sort the list
marks.sort()
print("sort:", marks)

# for reverse
marks.reverse()
print("reverse:", marks)

# clear the list
marks.clear()
print("clear:", marks)

marks = [22,44,22,32,42,12]

# count repeat element
print("count(22):", marks.count(22))

# copy the list
marks_copy = marks.copy()
print("copy:", marks_copy)

print(min(marks))
print(max(marks))
print(sum(marks))
print(len(marks))