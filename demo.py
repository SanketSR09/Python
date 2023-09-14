import threading

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial of {n} is {result}")

def square(n):
    result = n ** 2
    print(f"Square of {n} is {result}")

# Numbers for which we want to calculate factorial and square
numbers = [5, 7, 3, 8]

# Create thread objects for factorial and square functions
factorial_threads = []
square_threads = []

for num in numbers:
    factorial_thread = threading.Thread(target=factorial, args=(num,))
    square_thread = threading.Thread(target=square, args=(num,))
    
    factorial_threads.append(factorial_thread)
    square_threads.append(square_thread)

# Start the threads for factorial and square calculations
for factorial_thread in factorial_threads:
    factorial_thread.start()

for square_thread in square_threads:
    square_thread.start()

# Wait for all threads to finish
for factorial_thread in factorial_threads:
    factorial_thread.join()

for square_thread in square_threads:
    square_thread.join()

print("All threads have finished.")

