# STRINGS
#########################################################################################################

# Strings can be defined with either single or double quotes. It can be up to 255 characters long.
myName = 'Dakota' 
myMiddleName = "Natasha" 

multiLineString = '''
This 
is 
a 
multi-line 
string.
'''
print('\nmulti line string: ' + multiLineString)

quotes = 'She said, "Hello!"'
print('quotes formating: ' + quotes)

appostrophes = "It's a nice day!"
print('\napostrophe formating: ' + appostrophes)

backSlashQuotes = 'She said, "It\'s a nice day!"'
print('\nquotes formating with back slash:\n' + backSlashQuotes)

backSlashAppostrophes = "She said, \"It's a nice day!\"\n"
print('\napostrophe formating with back slash:\n' + backSlashAppostrophes)

isInString = 'hello' in 'hello world'
print('\nchecking to see if another string is in a string:\n' + str(isInString))

isNotInString = 'goodbye' not in 'hello world'
print('\nchecking to see if another string is not in a string:\n' + str(isNotInString))

lengthOfString = len(myName) # indexing
print('\nlength of string:\n' + str(lengthOfString) + '\n')

concatenateString = myName + myMiddleName
print(concatenateString)

print('letter of string at index 0:\n' + myName[0] + '\n')
print('letter of string at index -1:\n' + myName[-1] + '\n')
#print('letter of string at index 6:\n' + myName[6] + '\n') 
# # Note: This will raise an IndexError because the index is out of range. 
# The last index of the string is 


# Concatenating with the augmented assignment operator (+=)
myAgeInt = 29
myName += str(myAgeInt)

# String Interpolation: Inserting variables and expressions into a string

# F-Strings: formatted string literals that allow you to embed variables or expressions
# inside replacement fields that are indicated by curly braces {}.
# Note
nameAndAge = f'My name is {myName} and I am {myAgeInt} years old'
print(nameAndAge)

# String Slicing: extract a portion of a string or work with only a specific part
#string[start:stop]
print(myName[0:4]) # Dako
print(myName[1:4]) # ako starts at index 1 and extracts up to the letter at index 4
print(myName[:4]) # Dako extracts up to the letter at index 4
print(myName[3:]) # ota29 starts at 3rd index and Extracts everything after
print(myName[:]) # extracts entire string

# String[start:stop:step]
print(myName[0:5:2]) # Dkt starts at the first index, ends at the last, skips every 2
print(myName[::-1]) # 92atokaD puts characters backwards

# Return a new string with all characters converted to uppercase
myNameUpperCase = myName.upper()
print(myNameUpperCase)

# Return a new string with all characters converted to lowercase
myNameLowerCase = myName.lower()
print(myNameLowerCase)

# Return a new string with specified leading and trailing characters removed. 
# w/o arguments passed leading and trailing whitespace is removed
myNameStrip = myName.strip('D')
print(myNameStrip)

untrimmedStringWhiteSpace = '  ssssaaa  '
# Remove the whitespace
trimmedString = untrimmedStringWhiteSpace.strip()
print(trimmedString)

untrimmedString = 'ssssaaa'
# Remove the ssss
trimS = untrimmedString.strip('s')
print(trimS)

# Remove the aaa
trimA = untrimmedString.strip('a')
print(trimA)

 # Replace(old, new) returns a new string will all occurences of old replaced by new
newName = myName.replace('Dakota', 'Dabobba')
print(newName)

# split(seperator) splits a strong on a specific seperator into a list of strings.
# if no seperator indicated then it splits on whitespace
splitName = myName.split('a')
print(splitName)

# join(iterable) joins elements of an iterable into a string with a separator
joinedString = ' '.join(['Hello', 'World'])
print(joinedString)

# Examples of iterables that can be joined:
# Lists
myList = ['Python', 'is', 'great']
joinedList = ' '.join(myList)
print(joinedList) # prints 'Python is great' because the elements of the list are joined together with a space in between.

# Tuples
myTuple = ('Python', 'is', 'fun') 
joinedTuple = ' '.join(myTuple)
print(joinedTuple) # prints 'Python is fun' because the elements of the tuple are joined together with a space in between.

# Sets
mySet = {'Python', 'is', 'awesome'}     
joinedSet = ' '.join(mySet)
print(joinedSet) # prints 'Python is awesome' 
# Note: the order of the words may vary because sets are unordered collections.


# Dictionaries (joining keys)
myDict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
joinedDictKeys = ' '.join(myDict.keys())
print(joinedDictKeys) # prints 'name age city' because the keys of the dictionary are joined together with a space in between.
# Note: The order of keys in a dictionary is not guaranteed, so the output may vary.

# Dictionaries (joining values)
joinedDictValues = ' '.join(str(value) for value in myDict.values())
print(joinedDictValues) # prints 'Alice 30 New York' because the values of the dictionary are joined together with a space in between.
# Note: We convert values to strings because join() requires all elements to be strings.

# Dictionaries (joining key-value pairs)
joinedDictItems = ' '.join(f'{key}:{value}' for key, value in myDict.items())
print(joinedDictItems) # prints 'name:Alice age:30 city:New York' 
#because the key-value pairs of the dictionary are joined together with a space in between, 
# and each pair is formatted as 'key:value'.

# Dictionaries (joining key-value pairs with a different separator)
joinedDictItemsWithComma = ', '.join(f'{key}-{value}' for key, value in myDict.items())
print(joinedDictItemsWithComma) # prints 'name-Alice, age-30, city-New York' 
# because the key-value pairs of the dictionary are joined together with a comma and space 
# in between, and each pair is formatted as 'key-value'.

# Dictionaries (joining key-value pairs with a different separator and format)
joinedDictItemsWithSemicolon = '; '.join(f'{key}={value}' for key, value in myDict.items())
print(joinedDictItemsWithSemicolon) # prints 'name=Alice; age=30; city=New York' 
# because the key-value pairs of the dictionary are joined together with a semicolon and space
# in between, and each pair is formatted as 'key=value'.

# Dictionaries (joining key-value pairs with a different separator and format, and sorting by key)
joinedDictItemsSorted = '; '.join(f'{key}={value}' for key, value in sorted(myDict.items()))
print(joinedDictItemsSorted) # prints 'age=30; city=New York; name=Alice' 
# because the key-value pairs of the dictionary are joined together with a semicolon and space 
# in between, each pair is formatted as 'key=value', and the pairs are sorted by key.

# Dictionaries (joining key-value pairs with a different separator and format, and sorting by value)
joinedDictItemsSortedByValue = '; '.join(f'{key}={value}' for key, value in sorted(myDict.items(), key=lambda item: item[1]))
print(joinedDictItemsSortedByValue) # prints 'age=30; city=New York; name=Alice' 
# because the key-value pairs of the dictionary are joined together with a semicolon and space
# in between, each pair is formatted as 'key=value', and the pairs are sorted by value.

myDictList = {'name': ['Alice', 'Alex', 'Alicia'], 'age': [30, 31, 32], 'city': ['New York', 'Los Angeles', 'Chicago']}

# Joining key-value pairs of a dictionary where values are lists, with a different separator and format
joinedDictListValues = ' | '.join(f'{key}: {", ".join(str(value) for value in values)}' for key, values in myDictList.items())
print(joinedDictListValues) # prints 'name: Alice, Alex, Alicia | age: 30, 31, 32 | city: New York, Los Angeles, Chicago'
# because the key-value pairs of the dictionary are joined together with ' | ' in between,
# each pair is formatted as 'key: value1, value2, ...', and the values are joined together with a comma and space.

# Joining key-value pairs of a dictionary where values are lists, with a different separator and format, and sorting by key
joinedDictListValuesSorted = ' | '.join(f'{key}: {", ".join(str(value) for value in values)}' for key, values in sorted(myDictList.items()))
print(joinedDictListValuesSorted) # prints 'age: 30, 31, 32 | city: New York, Los Angeles, Chicago | name: Alice, Alex, Alicia'
# because the key-value pairs of the dictionary are joined together with ' | ' in between,
# each pair is formatted as 'key: value1, value2, ...', the values are joined together with a comma and space, 
# and the pairs are sorted by key.

# Joining key-value pairs of a dictionary where values are lists, with a different separator and format, and sorting by the length of the value lists
joinedDictListValuesSortedByLength = ' | '.join(f'{key}: {", ".join(str(value) for value in values)}' for key, values in sorted(myDictList.items(), key=lambda item: len(item[1])))
print(joinedDictListValuesSortedByLength) # prints 'name: Alice, Alex, Alicia | age: 30, 31, 32 | city: New York, Los Angeles, Chicago'
# because the key-value pairs of the dictionary are joined together with ' | ' in between,
# each pair is formatted as 'key: value1, value2, ...', the values are joined together with a comma and space,
# and the pairs are sorted by the length of the value lists 
# (in this case, all value lists have the same length, so the order is the same as the original dictionary).

# Printing each value of a dictionary where values are lists, with a different separator and format
for key, values in myDictList.items():
    print(f'{key}: {", ".join(str(value) for value in values)}') 
# prints each key followed by its list of values, with the values joined together with a comma and space.
# Output:
# name: Alice, Alex, Alicia
# age: 30, 31, 32
# city: New York, Los Angeles, Chicago

# Printing each value of a dictionary where values are lists, with a different separator and format, and sorting by key
for key, values in sorted(myDictList.items()):
    print(f'{key}: {", ".join(str(value) for value in values)}')
# prints each key followed by its list of values, with the values joined together with a comma and space, and the keys sorted alphabetically.
# Output:
# age: 30, 31, 32
# city: New York, Los Angeles, Chicago 
# name: Alice, Alex, Alicia

# startswith(prefix) returns True if the string starts with the specified prefix, otherwise False
startsWithMy = myName.startswith('My')
print(startsWithMy) # prints False because myName is 'Dakota29' and My is not the starting substring.

startsWithDak = myName.startswith('Dak')
print(startsWithDak) # prints True because myName is 'Dakota29' and Dak is the starting substring.

# endswith(suffix) returns True if the string ends with the specified suffix, otherwise False
endsWith29 = myName.endswith('29')
print(endsWith29) # prints True because myName is 'Dakota29' and 29 is the ending substring.
endsWithDak = myName.endswith('Dak')
print(endsWithDak) # prints False because myName is 'Dakota29' and Dak is not the ending substring.

# find(substring) returns the lowest index of the substring if it is found in the string, otherwise -1
indexOfOta = myName.find('ota')
print(indexOfOta) # prints 4 because 'ota' starts at index 4 in 'Dakota29'.
indexOfX = myName.find('x')
print(indexOfX) # prints -1 because 'x' is not found in 'Dakota29'.

# count(substring) returns the number of occurrences of the substring in the string
countOfA = myName.count('a')
print(countOfA) # prints 2 because there are two 'a's in 'Dakota29'.
countOfZ = myName.count('z')
print(countOfZ) # prints 0 because there are no 'z's in 'Dakota29'.

# capitalize() returns a new string with the first character capitalized and the rest lowercased
capitalizedName = myName.capitalize()
print(capitalizedName) # prints 'Dakota29' because the first character is already capitalized and the rest are unchanged.

# title() returns a new string with the first character of each word capitalized and the rest lowercased
titleName = myName.title()
print(titleName) # prints 'Dakota29' because there is only one word and the first character is already capitalized.

# swapcase() returns a new string with uppercase characters converted to lowercase and lowercase characters converted to uppercase
swapCaseName = myName.swapcase() 
print(swapCaseName) # prints 'dAKOTA29' because all uppercase letters are converted to lowercase and all lowercase letters are converted to uppercase.

# isalnum() returns True if all characters in the string are alphanumeric (letters and numbers) and there is at least one character, otherwise False
isAlnum = myName.isalnum()
print(isAlnum) # prints True because 'Dakota29' contains only letters and numbers.

# isalpha() returns True if all characters in the string are alphabetic (letters) and there is at least one character, otherwise False
isAlpha = myName.isalpha()
print(isAlpha) # prints False because 'Dakota29' contains numbers.

# isdigit() returns True if all characters in the string are digits and there is at least one character, otherwise False
isDigit = myName.isdigit()
print(isDigit) # prints False because 'Dakota29' contains letters.

# isspace() returns True if all characters in the string are whitespace and there is at least one character, otherwise False
isSpace = myName.isspace()
print(isSpace) # prints False because 'Dakota29' contains letters and numbers, not just whitespace.

# islower() returns True if all cahracters in the string are lowercase and there is at least one character, otherwise False
isLower = myName.islower()
print(isLower) # prints False because 'Dakota29' contains uppercase letters.

# isupper() returns True if all characters in the string are uppercase and there is at least one character, otherwise False
isUpper = myName.isupper()
print(isUpper) # prints False because 'Dakota29' contains lowercase letters.

# center(width, fillchar) returns a new string centered in a field of a given width, padded with the specified fill character (default is space)
centeredName = myName.center(20, '*')  
print(centeredName) # prints '*******Dakota29*******' because 'Dakota29' is centered in a field of width 20, with '*' used as the fill character on both sides.

