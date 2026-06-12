#function call it self

#fibonaci series

'''
0 1 1 2 3 5 8 13 21... 
0 1 2 3 4 5 6 07 08.....
# algorithum of fibonaci

fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
fib(4) = fib(2) + fib(3)
fib(n) = fib(n-2) + fib(n-1)

fib(n) = current number
fib(n-2) = its last to last number
fib(n-1) = for last number

'''

def fibonaci(n):
    #base case of recursion
    if(n == 0 or n == 1):
        return n
    else:
        return fibonaci(n-2) + fibonaci(n-1)
    
print(fibonaci(1))

#                               OR

def fibo(n):
    #base case of recursion
    if(n == 0 or n == 1):
        return n
    else:
        return fibo(n-2) + fibo(n-1)
    
def fiboo(n):
    for i in range(n + 1):
        print(fibo(i),end=" ")    

print(fiboo(10))




