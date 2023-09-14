# def sum(a=1,b=3):
#     add =a+b
#     subs=a-b
#     print("The addition is :",add)
#     print("The substration is :",subs)

# sum(100,45)

def average(*numbers):
    sum=0
    for i in numbers:
        sum= sum+i
    print("The average is :",sum/len(numbers))

average(10,10,10)