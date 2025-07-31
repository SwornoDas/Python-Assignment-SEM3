# Program to swap two numbers using a temporary variable (alternative method shown in comments)

# Input two numbers from the user
a = int(input("Enter first number. "))
b = int(input("Enter second number. "))

# Swapping using a temporary variable (uncomment below lines to use this method)
# c = a      # Store value of a in temporary variable c
# a = b      # Assign value of b to a
# b = c      # Assign value of c (original a) to b

# Swapping without using a temporary variable (current method)
a = a + b
b = a - b
a = a - b

# Display the swapped values
print("a is",a ,"\n","b is",b)