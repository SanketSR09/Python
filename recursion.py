# n= input("Enter the number whose factorial we want to calculate :")
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(3))

def fibonacchi(n):
   if n<=1:
      return n
   else:
      return (fibonacchi(n-1)+fibonacchi(n-2))
nterms=10
if nterms <=0:
   print("Please enter a positive integer")
else:
   print("fibonacchi series :")
   for i in range(nterms):
      print(fibonacchi(i))