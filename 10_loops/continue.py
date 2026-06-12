print('i < 10:')
for i in range(1,20):
    if i < 10:
        continue         #print < of 10 only
    print(i)

print('\ni > 10:')
for i in range(1,20):
    if i > 10:
        continue         #print > of 10 value only
    print(i)

print('\ni == 10:')
for i in range(1,20):
    if i == 10:
        continue         #cant print 10 and continue with 11 , skip 10 
    print(i)
