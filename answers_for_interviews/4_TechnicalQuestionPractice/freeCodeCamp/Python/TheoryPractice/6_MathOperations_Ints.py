# Mathematical Operations in Python
#########################################################################################################

print("\n*****************************************")
print("Mathematical Operations in Python")
print("*****************************************\n")



# Addition
print('ADDITION')
print(5 + 3) # Output: 8
print(f'{5} + {3} = {5 + 3}\n') # Output: 5 + 3 = 8

int_0 = -3
int_1 = 5

print(int_0 + int_1) # Output: 2
print(f'{int_0} + {int_1} = {int_0 + int_1}\n') # Output: -3 + 5 = 2


add = int_0 + int_1
print(add) # Output: 2  
print(str(int_0) + ' + ' + str(int_1) + ' = ' + str(add)) # Output: -3 + 5 = 2
#**************************************************************************



# Subtraction
print('\nSUBTRACTION')
print(5 - 3) # Output: 2
print(f'{5} - {3} = {5 - 3}\n') # Output: 5 - 3 = 2

print(int_0 - int_1) # Output: -8
print(f'{int_0} - {int_1} = {int_0 - int_1}\n') # Output: -3 - 5 = -8

subtract = int_1 - int_0 
print(subtract)
print(str(int_1) + ' - ' + str(int_0) + ' = ' + str(subtract))
#**************************************************************************



# Multiplication
print('\nMULTIPLICATION')
print(5 * 3) # Output: 15
print(f'{5} * {3} = {5 * 3}\n') # Output: 5 * 3 = 15

print(int_0 * int_1) # Output: -15
print(f'{int_0} * {int_1} = {int_0 * int_1}\n') # Output: -3 * 5 = -15

multiply = int_1 * int_0
print(multiply)
print(str(int_1) + ' * ' + str(int_0) + ' = ' + str(multiply)) # Output = 5 * -3 = -15
#**************************************************************************



# Division
print('\nDIVISION')
print(5 / 3) # Output: 1.6666666666666667
print(f'{5} / {3} = {5/3}\n') # Output: 5 / 3 = 1.6666666666666667

print(int_0 / int_1) # Output: -0.6
print(f'{int_0} / { int_1} = {int_0 / int_1}\n') # Output: -3 / 5 = -0.6

divide = int_1 / int_0
print(divide) # Output: -1.6666666666666667
print(str(int_1) + ' / ' + str(int_0) + ' = ' + str(divide)) # Output: 5 / -3 = -1.6666666666666667
#**************************************************************************



# Floor Division: Divide and round down to nearest whole number (negatives keep going to negative infinity)
print('\nFLOOR DIVISION')
print(5 // 3) # Output: 1
print(f'{5} // {3} = {5 // 3}\n') # Output: 5 // 3 = 1

print(int_0 // int_1) # Output: -1
print(f'{int_0} // {int_1} = {int_0 // int_1}\n') # Output: 5 / -3 = -1.6666666666666667

floorDivide = int_1 // int_0
print(floorDivide) # Output: -2
print(str(int_1) + ' // ' +  str(int_0) + ' = ' + str(floorDivide)) # Output: 5 // -3 = -2
#**************************************************************************



# Modulo: a mod b, divide a by b and return the remainder
print('\nMODULO')
print(5 % 3) # Output: 2
print(f'{5} % {3} = {5 % 3}\n') # Output: 5 % 3 = 2

print(int_0 % int_1) # Ouput: 2
print(f'{int_0} % {int_1} = {int_0 % int_1}\n') # Output: -3 % 5 = 2

modulo = int_1 % int_0
print(modulo) # Output: -1
print(str(int_1) + ' % ' + str(int_0) + ' = ' + str(modulo)) # Output: 5 % -3 = -1
#**************************************************************************



# Exponentiation
print('\nEXPONENTIATION')
print(5 ** 3) # Output: 125
#**************************************************************************



# Operator Precedence
print('\nOPERATOR PRECEDENCE')
print(5 + 3 * 2) # Output: 11 (Multiplication is performed before addition)
print((5 + 3) * 2) # Output: 16 (Parentheses change the order of operations)
#**************************************************************************



# Augmented Assignment Operators
print('\nAUGMENTED ASSIGNMENT OPERATORS')
x = 5
x += 3 # Equivalent to x = x + 3
print(x) # Output: 8

x *= 2 # Equivalent to x = x * 2
print(x) # Output: 16

x /= 4 # Equivalent to x = x / 4
print(x) # Output: 4.0

x -= 1 # Equivalent to x = x - 1
print(x) # Output: 3.0

