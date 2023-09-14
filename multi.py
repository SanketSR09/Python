import threading
import math

# def task_function(multi):
#     for i in range(10):
#         print(f"{multi} is executing {i}")

def square(num):
    result=num**2
    print(f"{num} is {result}")
def factorial(num):
    result=1
    for i in range(1,num+1):
        result *=i
        print(f"The Factorial of {num} is {result}")

numbers=[1,2,3,4,5]

for num in numbers:
    thread1=threading.Thread(target=square, args=(num,))
    thread2=threading.Thread(target=factorial, args=(num,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All thread are executed")
