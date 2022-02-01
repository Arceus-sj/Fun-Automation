# lists == arrays with some condition
items = ["Pen", "Books", "Paper", "Bags"]
print(items[0])

print(items)
items[1] = "Notebooks"

print(items)

# find length of list
print(len(items))

# list() constructor
myList = list(("apple", "banana", "mango"))
print(myList)

# insert() item to particular index
myList.insert(2, "cherry")
print(myList)

# append() adding item at the end of list
myList.append("orange")
print(myList)

# remove() method removes the specified items
myList.remove("cherry")
print(myList)

# del keyword remove the item from specific index
del myList[-1]
print(myList)

# clear() method to empties the list
myList.clear()
print(myList)

# jion two list
myList = list(("mango", "banana"))
myList2 = list(("potato", "tomato"))
totalItems = myList + myList2
print(totalItems)


# search in list
print("banana" in totalItems)
print("apple" in myList)