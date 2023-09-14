with open('example.txt','w') as file:
    file.write("This is Sanket Rangari.\n")

with open('example.txt','r') as file:
    content=file.read()
    print(content)

with open("example.txt","a") as file:
    file.write("And I am 21.")

with open ("example.txt",'r') as file:
    content= file.read()
    print(content)

with open('example.txt','r') as file:
    lines=file.readlines()
    for line in lines:
        print(line)