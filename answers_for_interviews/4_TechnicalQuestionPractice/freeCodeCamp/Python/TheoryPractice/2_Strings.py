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

