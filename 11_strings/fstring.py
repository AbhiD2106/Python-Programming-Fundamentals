#string formatting
# strings are immutable
# immutable = notchangable
temp = "hey {} , you are wonderfull,take {}$"

a = "abhi"
a1 = 10000
b = "dhruvii"
b1 = 211213

s1 = temp.format(a,a1)
print(s1)
s2 = temp.format(b,b1)
print(s2)

                    #or

print(f"{a} you are good,take {a1}$")