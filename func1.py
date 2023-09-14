def calculate(a,b):
    sum = a+b
    print(sum)

def isGreater(a,b):
    if(a>b):
        print(a," is greater number.")
    elif(a==b):
        print("Both are equal.")
    else:
        print(b,"is greater number.")

def avrage(a,b):
    avg=(a+b)/2
    print(avg)

a=12
b=12
isGreater(a,b)
calculate(a,b)
avrage(a,b)

c=12
d=45
isGreater(c,d)
calculate(c,d)
avrage(c,d)