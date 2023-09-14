#immutable i.e. it can't be changed(no insertion and removal of data)

#we need to give ',' after the element if we want to give a single element in tuple if we dont give ',' then it will be shown as list 
t1=(1,2,"sanket",5,True)
print(type(t1))
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])

#length
print(len(t1))

countries=("India","Spain","Italy","Australia")
# if we want to change the tuple we cannot change tuple directly we need to create another list and after that vconvert that list into tuple as given below
temp=list(countries)
#insertion
temp.append("England")
#deletion
temp.pop(3)
#change items
temp[2]="West Indies"
# converted list into tuple
countries= tuple(temp)
print(countries)


#concatination
countries2=("Bangladesh","Europe")
c=countries+countries2
print("The concatination of both the tupel is :",c)

#methods
print(countries.count("India")) #count method

#if we wnant to know the index of an element then we use index method
x=t1.index("sanket")
print(x) #index method

# x=t1.index(a,i1,i2) here a = the element we want to find, i1= the starting index from where we want to start the search of index, i2= ending index form where we want to end the searching of element
#also tuple.index(element, start , end)
x=countries.index("India",0,4)
print(x) 