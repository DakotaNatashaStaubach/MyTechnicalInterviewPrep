# INTRO TO PYTHON
#########################################################################################################

#********************************************************************************************************
# VARIABLES & DATA TYPES
#********************************************************************************************************
# Variables are used to store data.

# Note: 
# 1. Variable names can only start with a letter or an underscore. 
# 2. They cannot start with a number. 
# 3. They can only contain letters, numbers, and underscores. 
# 4. They are case-sensitive.
# 5. They cannot be a reserved keyword in Python.
# If any of these rules are violated, a SyntaxError will be raised.

# Strings
myName = 'Dakota' 
myMiddleName = "Natasha" 
multiLineString = '''
This 
is 
a 
multi-line 
string.
'''
quotes = 'She said, "Hello!"'
appostrophes = "It's a nice day!"
backslashQuotes = 'She said, "It\'s a nice day!"'
backslashAppostrophes = "She said, \"It's a nice day!\"\n"
isInString = 'hello' in 'hello world'
isNotInString = 'goodbye' not in 'hello world'
lengthOfString = len(myName) # indexing

# Note: Strings can be defined with either single or double quotes. It can be up to 255 characters long.

# Integers
myAgeInt = 29 
# Note: Integers are whole numbers. They can be of any length. 

# Floats
myHeight = 5.25
myWeight = 160.553553553553553553 
# Note: Floats are numbers with up to 15 decimal places. 
# It will round to the nearest 15th decimal place if more than 15 decimal places are provided.

# Booleans
isStudent = False
# Note: Booleans can only be True or False. 
# They are used to represent the truth value of an expression.

# Sets
mySet = {7,5, 8, 6, 9}
# Note: Sets are unordered collections of unique elements. 
# They are defined with curly braces {}.
# Sets do not allow duplicate elements. If a duplicate element is added to a set, it will be ignored.
# Sets are mutable, meaning that their values can be changed after they are created.
# Sets can be used to perform mathematical operations like union, intersection, difference, and symmetric difference.
# Sets can also be used to remove duplicate elements from a list.
# For example, if you have a list with duplicate elements, you can convert it to a set to remove the duplicates, and then convert it back to a list if needed.
myListWithDuplicates = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
mySetFromList = set(myListWithDuplicates)
myListWithoutDuplicates = list(mySetFromList)

# Lists
myList = [1, 2, 3, 4, 5]
# Note: Lists are ordered collections of elements. 
# They can contain duplicate elements.
# They are mutable, meaning that their values can be changed after they are created.
# They can contain elements of different data types.
# They are defined with square brackets [].
# Elements in a list are separated by commas.
# The elements in a list are indexed, meaning that they can be accessed by their position in the list.
# The first element in a list has an index of 0, the second element has an index of 1, and so on.
# The last element in a list can be accessed with an index of -1. 
# The second to last element can be accessed with an index of -2.
# Lists can also be nested, meaning that they can contain other lists as elements.
# 

# Dictionaries
myDict = {'name': 'Dakota', 'age': 29, 'height': 5.25, 'weight': 160.553553553553553553, 'isStudent': False}
# Note: Dictionaries are unordered collections of key-value pairs. 
# They are defined with curly braces {}.
# The key-value pairs are separated by a colon :.

# Tuples
myTuple = (1, 2, 3, 4, 5)
# Note: Tuples are ordered collections of elements. 
# They are defined with parentheses (). 
# They are immutable, meaning that their values cannot be changed after they are created.

# Ranges
myRange = range(1, 10)
# Note: Ranges are used to generate a sequence of numbers. 
# They are defined with the range() function. 
# The range() function takes three arguments: start, stop, and step. 
# The start argument is the starting number of the sequence (inclusive), 
# the stop argument is the ending number of the sequence (exclusive), 
# and the step argument is the increment between each number in the sequence. 
# If the step argument is not provided, it defaults to 1.





#********************************************************************************************************
#PRINTING VARIABLES
#********************************************************************************************************
print("\n*****************************************")
print("PRINTING VARIABLES")
print("*****************************************\n")
print('string: ' + myName)
print('int: ' + str(myAgeInt))
print('float: ' + str(myHeight))
print('float with more than 15 decimal places: ' + str(myWeight))
print('boolean: ' + str(isStudent) + '\n')
print(myName, myAgeInt, myHeight, isStudent)
print('\nmulti line string: ' + multiLineString)
print('quotes formating: ' + quotes)
print('\napostrophe formating: ' + appostrophes)
print('\nquotes formating with back slash:\n' + backslashQuotes)
print('\napostrophe formating with back slash:\n' + backslashAppostrophes)
print('\nchecking to see if another string is in a string:\n' + str(isInString))
print('\nchecking to see if another string is not in a string:\n' + str(isNotInString))
print('\nlength of string:\n' + str(lengthOfString) + '\n')
print('letter of string at index 0:\n' + myName[0] + '\n')
#print('letter of string at index 6:\n' + myName[6] + '\n') 
# # Note: This will raise an IndexError because the index is out of range. 
# The last index of the string is 5.

print('letter of string at index 5:\n' + myName[5] + '\n')
print('letter of string at index -1:\n' + myName[-1] + '\n')
print('letter of string at index -6:\n' + myName[-6] + '\n') 
# Note: This will not raise an index error because the index is within the range of the string. 
# The first index of the string is -6.




#********************************************************************************************************
# TYPING, TYPE CASTING, & TYPE ERRORS
#********************************************************************************************************
print("\n*****************************************")
print("TYPING, TYPE CASTING, & TYPE ERRORS")
print("*****************************************\n")

# Python is DYNAMICALLY typed so variable types don't need to be explicitly declared. 
# The types are implicitly determined by the value assigned to the variable.
# Types are determined at runtime. 
# Type errors are detected when a program runs, not when it is compiled.

# Type Casting
myAgeString = str(myAgeInt)
myAgeFloat = float(myAgeInt)
# Notes: Type casting is the process of converting a variable from one data type to another. 
# Type casting can be done using built-in functions like str(), int(), float(), bool(), etc.

# Concatenating variables with strings and type casting the integer variable to a string variable.
print('My name is ' + myName + ' and I am ' + myAgeString + ' years old.')
# Note: type casting str(myAgeInt) is necessary to concatenate the integer variable with the string.

# Type Getting
print (type(myName))
print (type(myAgeInt))
print (type(myHeight))
print (type(isStudent))
print (type(mySet))
print (type(myList))
print (type(myDict))
print (type(myTuple))
print (type(myRange))

print (isinstance(myName, str))
print (isinstance(myAgeInt, int))



# Python is also STRONGLY typed, meaning that it does not allow implicit type conversion.
# For example, if you try to concatenate a string and an integer without type casting, a TypeError will be raised.

# Type Errors 
# (uncomment the following lines one at a time to see the TypeErrors)

# The following will NOT raise a TypeError because we are concatenating two string variables.
print(myName + myMiddleName)  

# The following will raise a TypeError because we are trying to subtract a string from an integer.
#print(myName - myAgeInt)

# The following will raise a TypeError because we are trying to concatenate a string and an integer without type casting.
#print(myName + myAgeInt)

# The following will NOT raise a TypeError because we are multiplying a string by an integer. 
print(myName *3) 

# The following will raise a TypeError because we are trying to multiply a string by another string.
#print(myName * myMiddleName)

# The following will raise a TypeError because we are trying to multiply a string by a float.
#print(myName * 3.5)

# The following will raise a type error because range only accepts integer arguments, not float arguments.
#for i in range(myHeight):
    #print(i)

# The following will NOT raise a TypeError because we are type casting the float variable to an integer variable.
for i in range(int(myHeight)):
    print(i)



#********************************************************************************************************
# PRACTICE: BUILDING A REPORT CARD PRINTER
#********************************************************************************************************
print("\n*****************************************")
print("PRACTICE: BUILDING A REPORT CARD PRINTER")
print("*****************************************\n")

name = 'Alice'
print(name)
print(type(name))
print(name, type(name))

is_student = True
print(is_student, type(is_student))

age = 20
print(age, type(age))

score = 80.5
print(isinstance(score, int))
print(isinstance(score, float))
print(score, type(score))

#********************************************************************************************************
# OPERATORS
#********************************************************************************************************
print("\n*****************************************")
print("OPERATORS")
print("*****************************************\n")