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
# Note: Strings can be defined with either single or double quotes. It can be up to 255 characters long.

# Integers
myAgeInt = 29 
# Note: Integers are whole numbers. They can be of any length. 
# Immutable

# Floats
myHeight = 5.25
myWeight = 160.553553553553553553 
# Note: Floats are numbers with up to 15 decimal places. 
# It will round to the nearest 15th decimal place if more than 15 decimal places are provided.
# Immutable

# Booleans
isStudent = False
# Note: Booleans can only be True or False. 
# They are used to represent the truth value of an expression.
# Imutable 

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
# Immutable

# Sets
mySet = {7,5, 8, 6, 9}
# Note: Sets are unordered collections of unique elements. 
# They are defined with curly braces {}.
# Elements in a set are separated by commas.

# Lists
myList = [1, 2, 3, 4, 5]
# Note: Lists are ordered collections of elements. 
# They are defined with square brackets [].
# Elements in a list are separated by commas.

# Dictionaries
myDict = {'name': 'Dakota', 'age': 29, 'height': 5.25, 'weight': 160.553553553553553553, 'isStudent': False}
# Note: Dictionaries are unordered collections of key-value pairs. 
# They are defined with curly braces {}.
# The key-value pairs are separated by a colon :.



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
5.
print('letter of string at index 5:\n' + myName[5] + '\n')
print('letter of string at index -1:\n' + myName[-1] + '\n')
print('letter of string at index -6:\n' + myName[-6] + '\n') 
# Note: This will not raise an index error because the index is within the range of the string. 
# The first index of the string is -6.










