#unordered collection of data items. They store multiple items in a single variable. Set items are seperarted by commas anndd enclosed within curly braces. SEts are unchangable, meaning you cannot change items of the set once creatted. sets donot contain duplicate items.

s1={1,2,3,4,5,1}
print(s1)
items={"carla",39,False,3.4,10}
print(items)
print(len(s1))
sanket=set()
print(type(sanket))

s2={3,5,6}
print(s1.union(s2))#used to merge two set 
print(s1,s2)

print(s1.update)