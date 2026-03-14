# LISTS IN PYTHON
#########################################################################################################
# Lists
# Lists are ordered collections of elements. 
# Since lists are ordered, the elements in a list have a specific order and can be accessed by an index.
# They are defined with square brackets [].
# Elements in a list are separated by commas.
myList = [1, 2, 3, 4, 5]
anotherList = ['apple', 'banana', 'cherry']

# They can contain duplicate elements.
duplicateList = [1, 2, 2, 3, 4, 4, 5]
print(duplicateList) # Output: [1, 2, 2, 3, 4, 4, 5]

# They are mutable, meaning that their values can be changed after they are created.
# For example, you can change the value of the first element in the list myList to 10 by using the index of the element.
myList[0] = 10
print(myList) # Output: [10, 2, 3, 4, 5]

# Another way to change the value of an element in a list is to use the append() method to add a new element to 
# the end of the list.
myList.append(6)
print(myList) # Output: [10, 2, 3, 4, 5, 6]

# Another way to change the value of an element in a list is to use the insert() method to add a new element at 
# a specific index in the list.
myList.insert(1, 15)
print(myList) # Output: [10, 15, 2, 3, 4, 5, 6]

# Another way to change the value of an element in a list is to use the remove() method to remove an element from 
# the list.
myList.remove(15)
print(myList) # Output: [10, 2, 3, 4, 5, 6]

# Another way to change the value of an element in a list is to use the pop() method to remove an element from 
# the list and return its value.
poppedElement = myList.pop(0)
print(poppedElement) # Output: 10
print(myList) # Output: [2, 3, 4, 5, 6]

# Another way to change the value of an element in a list is to use the sort() method to sort the elements in the
# list in ascending order.
myList.sort()
print(myList) # Output: [2, 3, 4, 5, 6]

# Another way to change the value of an element in a list is to use the reverse() method to reverse the order of
# the elements in the list.
myList.reverse()
print(myList) # Output: [6, 5, 4, 3, 2]

# Another way to change the value of an element in a list is to use the clear() method to remove all elements from
# the list.
myList.clear()
print(myList) # Output: []

# Another way to change the value of an element in a list is to use the extend() method to add all elements from
# another list to the end of the list.
myList.extend(anotherList)
print(myList) # Output: ['apple', 'banana', 'cherry']

# Here is a way to find the index of a specific element in the list. 
indexOfBanana = myList.index('banana')
print(indexOfBanana) # Output: 1

# Here is a way to count the number of times a specific element appears in a list.
countOfApple = myList.count('apple')
print(countOfApple) # Output: 1

# Here is a way to check if a specific element exists in a list.
isCherryInList = 'cherry' in myList
print(isCherryInList) # Output: True

# Here is a way to check if a specific element does not exist in a list.
isGrapeNotInList = 'grape' not in myList
print(isGrapeNotInList) # Output: True 

# Here is a way to find the length of a list.
lengthOfList = len(myList)

# Here is a way to access an element in a list by its index.
firstElement = myList[0]
print(firstElement) # Output: 'apple'

# Here is a way to access the last element in a list by using a negative index.
lastElement = myList[-1]
print(lastElement) # Output: 'cherry'

# Lists can contain elements of different data types.
mixedList = [1, 'apple', 3.14, True]

# Lists can also be nested, meaning that they can contain other lists as elements.
nestedList = [1, 2, [3, 4], 5]

# Lists can be sliced to create a new list that contains a subset of the elements in the original list.
slicedList = myList[1:3] 
print(slicedList) # Output: ['banana', 'cherry']
# This will create a new list that contains the elements at index 1 and 2 of the original list.
# The syntax for slicing a list is list[start:stop], 
# where start is the index of the first element to include in the slice,
# and stop is the index of the first element to exclude from the slice.


# Lists can also be sliced with a step to create a new list that contains every nth element in the original list.
slicedListWithStep = myList[0:3:2] 
print(slicedListWithStep) # Output: ['apple', 'cherry']
# This will create a new list that contains the elements at index 0 and 2 of the original list.
# The syntax for slicing a list with a step is list[start:stop:step],
# where start is the index of the first element to include in the slice,
# stop is the index of the first element to exclude from the slice, 
