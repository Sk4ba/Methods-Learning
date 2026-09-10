#collection = single "variable" used to store multiple values (basically an array)

#List = [] ordered and changeable. Duplicates OK
#Set = {} unordered and immutable, but Add/Remove OK, NO duplicates
#Tuple = () ordered and unchangeable, Duplicates OK. FASTER


#You may use the help function to get more info on what methods you can use
#print(help(collection-variable))

#List
print("---List---") #Use when you constantly add/remove/update elements
fruitsList = ["Apple", "Orange", "Banana", "Coconut"]
fruitsList.append("Pineapple") #adds an element to the end of the list
fruitsList.remove("Apple") #or u can do indexing too.
fruitsList.insert(0, "Pineapple") #inserts an element on a given index
fruitsList.sort() #sorts it alphabetically
#.reverse() = reverses the list
#.clear() = clears the list
print(fruitsList.index("Orange")) #prints what index is a specific element

for x in range(0,4):
    print(fruitsList[x])


print("\n---Set---") #Use when you need to store a lot of the same thing
fruitsSet = {"Apple", "Orange", "Banana", "Coconut"}
fruitsSet.add("Pineapple") #adds element
fruitsSet.remove("Apple") #removes an element
fruitsSet.pop() #remove the first element (random)
# fruitsSet.clear() = clears the set
print(fruitsSet)


print("\n---Tuple---") #Use when data shouldn't change
fruitsTuple = ("Apple", "Orange", "Banana", "Coconut", "Coconut")
print("Pineapple" in fruitsTuple) #shows if an element is in the tuple
print(fruitsTuple.index("Apple")) #shows index of an element
print(fruitsTuple.count("Coconut")) #counts how many is a specific element in tuple

for fruit in fruitsTuple:
    print(fruit)