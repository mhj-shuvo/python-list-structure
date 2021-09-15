# Script Bigins

# List structure
myList = []                     # Creting a empty list
print (myList)

myList = [1, 2, "string", 1.5]  # Creating list with values
print (myList)

myList.append("string")         # Adding new item to the list
print (myList)

myList.append([40, 50, "List"]) # Adding a list as a single item
print (myList)

myList.extend([1, 2, 3])        # Adding multiple item to the list
print (myList)

myList.insert(1, "newItem")     # Inserting new item at defined index
print (myList)

del myList[1]                   # Deleting item from defined index
print (myList)

myList.remove("string")         # Deleting first matched item from list
print (myList)

myList.pop()                    # Removes the last item
print (myList)

myList.pop(2)                   # Removes the item from defined index
print (myList)

print (myList)                  # Printing all items at a time
print (myList[2])               # Prints only the item defined by index
print (myList[:2])              # Prints items from starting to before the defined index
print (myList[1:3])             # Prints items from 1st defined index to before the 2nd defined index
print (myList[::1])             # Access all items in forward sequence
print (myList[::-1])            # Access all items in reverse sequnce

print (len(myList))             # Provides the length or number of items of the list
print (myList.index(2))         # Provides the index of first matched with items
print (myList.count(1))         # Provids the number of matches of provided value with items

myList.clear()                  # Removes all items from list
print (myList)

# Script Ends