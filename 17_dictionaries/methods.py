students = {"name": "abc", "age": 20, "courses": ["maths", "science"]}
print(students)
print(students["courses"][0])

print(students.get("age"))
print(students.get("phone", "not found"))  # if key not found it will return none or default value
students["phone"] = "1234567890"  # add new key value pair  
print(students)

students.update({"name": "xyz", "age": 21, "city": "new york"})  # update multiple key value pairs
print(students)

del students["age"]  # delete key value pair
print(students) 

students.pop("courses")  # delete key value pair and return value
print(students)

print(students.keys())  # return all keys
print(students.values())  # return all values
print(students.items())  # return all key value pairs as tuples

for key, value in students.items():  # iterate through dictionary
    print(key, value)
students.clear()  # clear all key value pairs

print(students) 

#disctionary comprehension
#table of five

table = {i: i*5 for i in range(1, 11)}
print(table)
