#mutable i.e insertion and deletion can be done
l=[1,2,3]
print(l)

#to know the type of given variable
print(type(l))

# #positive index
print(l[len(l)-2])

# #negative index
print(l[-2])

# #to insert elements into list
l.append(4)
print(l)
l.append(5)
print(l)

# #to print length of given list
print(len(l))

# #to print full list
print(l[:])

#to remove element from list
l.remove(3)
print(l)

#jump index
print(l[1:5:2])

#list Comprehension
l1=[i*i for i in range(6) if(i%2==0)]
print(l1)
l1=[i*i for i in range(6) if(i%2!=0)]
print(l1)

#sort 
l.sort(reverse=True)
print(l)

#insert into a list
l.insert(0,6)
print(l)

#extend method
m=[23,45]
l.extend(m)
print(l)