#operators
#Arithematic operators:
#Arithmetic operators perform mathematical operations like addition, subtraction, multiplication, division, etc 
#example:
x = 10  # Assigning the value 10 to the variable x
y = 5   # Assigning the value 5 to the variable y

print(x + y)  # Addition: Output will be 15 (10 + 5)
print(x - y)  # Subtraction: Output will be 5 (10 - 5)
print(x * y)  # Multiplication: Output will be 50 (10 * 5)
print(x / y)  # Division: Output will be 2.0 (10 / 5)
print(x % y)  # Modulus: Output will be 0 (10 % 5)
print(x ** y) # Exponentiation: Output will be 100000 (10^5)
print(x // y) # Floor Division: Output will be 2 (10 // 5)
# comparison operators:
#comparison operators compare the values of two operands and returns a boolean results (true or false).
#example:
x = 10
y = 5

print(x > y)  # Output: True (10 is greater than 5)
print(x < y)  # Output: False (10 is not less than 5)
print(x ** y == x)  # Output: False (10 raised to the power of 5 is not equal to 10)
print(x != y)  # Output: True (10 is not equal to 5)
print(x >= y)  # Output: True (10 is greater than or equal to 5)
print(x <= y)  # Output: False (10 is not less than or equal to 5)

#Logical operators:
#Logical operators perform logical operations like AND, OR, and NOT
#examples:
x = True
y = False

print(x and y)  # Output: False (True and False is False)
print(x or y)   # Output: True (True or False is True)
print(not x)    # Output: False (not True is False)

#Assignment operators:
#assignment operators are used to assign values to variables.
x = 10
x += 5  # This is equivalent to x = x + 5. So, x becomes 15.
x -= 3  # This is equivalent to x = x - 3. So, x becomes 12.
x *= 2  # This is equivalent to x = x * 2. So, x becomes 24.

#bitwise operators:
#bitwise operators performs bitwise operators on integers at the binary level.
#example:
x = 10  # Binary: 1010
y = 4   # Binary: 0100

print(x & y)   # Bitwise AND: Output: 0 (1010 & 0100 = 0000)
print(x | y)   # Bitwise OR: Output: 14 (1010 | 0100 = 1110)
print(x ^ y)   # Bitwise XOR: Output: 14 (1010 ^ 0100 = 1110)
print(~x)      # Bitwise NOT: Output: -11 (Complement of 1010 in two's complement representation)
print(x << 1)  # Bitwise Left Shift: Output: 20 (1010 shifted left by 1 becomes 10100)
print(x >> 1)  # Bitwise Right Shift: Output: 5 (1010 shifted right by 1 becomes 0101)

#membership operators:
#membership operators are used to test if a sequence (such as a string, list, or tuple) contains a specific
#example:
x = [1, 2, 3, 4, 5]  # Corrected closing bracket
print(3 in x)        # Output: True
print(6 not in x)    # Output: True

#identify operators:
#indentify operators are used to compare the memory locations of to objects.
#example:
#Using is operator:
x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)  # Output: False, because x and y refer to different memory locations
#using is not operator:
a = "hello"
b = "world"

print(a is not b)  # Output: True, because a and b are stored in different memory locations
#example:
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is z)  #output: true
print(x is y)  #output: false
print(x is not y)  #output:true

#bitwise AND (&):
#The bitwise AND operator perform a logical AND operation on each pair of correspoing bits of the operands
#The result is 1 if both bits are 1, otherwise,it's 0.
#example:
x = 10  # binary: 1010
y = 4   # binary: 0100

# Bitwise AND
print(x & y)  # Output: 0 (binary: 0000)

# Bitwise OR
print(x | y)  # Output: 14 (binary: 1110)

# Bitwise XOR
print(x ^ y)  # Output: 14 (binary: 1110)

# Bitwise NOT
print(~x)     # Output: -11 (binary: ...11110101)

# Bitwise Left Shift
print(x << 1)  # Output: 20 (binary: 10100)

# Bitwise Right Shift
print(x >> 1)  # Output: 5 (binary: 101)


