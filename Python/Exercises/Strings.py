# Create a variable and assign it the string "Just do it!"
# Access the "!" from the variable by index and print() it
# Print the slice "do" from the variable
# Get and print the slice "it!" from the variable
# Print the slice "Just" from the variable
# Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.

to_slice = "Just do it!"
print(to_slice[10])   # prints "!"
print(to_slice[5:7])  # prints "do"
print(to_slice[8:])   # prints "it!"
print(to_slice[:4])   # prints "Just"
print("Don't " + to_slice[5:])  # prints "Don't do it!"
