# SETS IN PYTHON
#########################################################################################################

mySet = {7,5, 8, 6, 9}
# Note: Sets are unordered collections of unique elements. 
# Since sets are unordered, the elements in a set do not have a specific order and cannot be accessed by an index.
# They are defined with curly braces {}.


# Sets do not allow duplicate elements. If a duplicate element is added to a set, it will be ignored.
# For example, if you try to add the number 7 to the set mySet, it will not be added because it is already in the set.
mySet.add(7) # This will not change the set because 7 is already in the set.
print(mySet) # Output: {7, 5, 8, 6, 9}

# Sets can also be used to remove duplicate elements from a list.
# For example, if you have a list with duplicate elements, you can convert it to a set to remove the duplicates, 
# and then convert it back to a list if needed.
myListWithDuplicates = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
mySetFromList = set(myListWithDuplicates)
myListWithoutDuplicates = list(mySetFromList)
print(myListWithoutDuplicates) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sets are mutable, meaning that their values can be changed after they are created.
# For example, you can add a new element to the set mySet using the add() method.
mySet.add(10) # This will add the number 10 to the set.
print(mySet) # Output: {7, 5, 8, 6, 9, 10}

# Sets can be used to perform mathematical operations like union, intersection, difference, and symmetric difference.
# For example, if you have two sets, you can find the UNION of the two sets by using the union() method or 
# the | operator.
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
unionSet = setA.union(setB)
unionSetWithOperator = setA | setB 
print(unionSet) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(unionSetWithOperator) # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# You can find the INTERSECTION of the two sets by using the intersection() method or the & operator.
intersectionSet = setA.intersection(setB)
intersectionSetWithOperator = setA & setB
print(intersectionSet) # Output: {4, 5}

# You can find the DIFFERENCE of the two sets by using the difference() method or the - operator.
# The difference of setA and setB is the set of elements that are in setA but not in setB.
differenceSet = setA.difference(setB)
differenceSetWithOperator = setA - setB
print(differenceSet) # Output: {1, 2, 3}

# You can find the SYMMETRIC DIFFERENCE of the two sets by using the symmetric_difference() method or the ^ operator.
# The symmetric difference of setA and setB is the set of elements that are in either setA or setB but not in both.
symmetricDifferenceSet = setA.symmetric_difference(setB)
symmetricDifferenceSetWithOperator = setA ^ setB
print(symmetricDifferenceSet) # Output: {1, 2, 3, 6, 7, 8}

# Sets can also be used to perform mathematical operations on lists.
# For example, if you have two lists, you can find the UNION of the two lists by converting them to sets and 
# using the union() method or the | operator.
listA = [1, 2, 3, 4, 5]
listB = [4, 5, 6, 7, 8]
unionList = list(set(listA).union(set(listB)))
unionListWithOperator = list(set(listA) | set(listB))
print(unionList) # Output: [1, 2, 3, 4, 5, 6, 7, 8]
print(unionListWithOperator) # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Sets can also be used to check for membership in a collection.
# For example, you can check if a number is in the set mySet using the in keyword.
print(5 in mySet) # Output: True
print(11 in mySet) # Output: False


