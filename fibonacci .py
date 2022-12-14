
#Fibonacci using for loop
n=int(input("Enter The No Of terms:"))

a=0
b=1
c=0
print("Fibonacci Series:",end=" ")
for i in range (n):
       print(c, end=" ")
       a=b
       b=c
       c=a+b
# fibonacci recursive method

def fibonacci(a):
       if a <= 1:
              return a
       else:
              return (fibonacci(a - 1) + fibonacci(a - 2))
a = int(input('Enter the value of n :'))
print('The term', a, 'in the fibonacci series is', fibonacci(a))
for i in range(a):
       print(fibonacci(i),end=' ')



