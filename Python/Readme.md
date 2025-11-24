
#### variable

- A variable is a name that stores a value in programming.

##### Types of values variables can store

```bash
number = 25          # integer
price = 99.99        # float
name = "name"       # string
is_active = True     # boolean
items = ["apple"]    # list
```


#### Math Operators
- Math operators (arithmetic operators) allow you to perform calculations.

    | Operator | Example  | Meaning                          |
    | -------- | -------- | -------------------------------- |
    | `+`      | `5 + 3`  | Addition                         |
    | `-`      | `5 - 3`  | Subtraction                      |
    | `*`      | `5 * 3`  | Multiplication                   |
    | `/`      | `5 / 3`  | Division (gives float)           |
    | `//`     | `5 // 3` | Floor division (removes decimal) |
    | `%`      | `5 % 3`  | Modulus (remainder)              |
    | `**`     | `5 ** 3` | Power/exponent (5³ = 125)        |


#### round the value

```bash
result = 10 + 3.7      # sum = 13.7
rounded_result = round(result)   # 14
result = 10 + 3.7      # sum = 13.7
rounded_result = round(result)   # 14
```


#### string
- A string in Python is a sequence of characters—letters, numbers, symbols, or spaces—surrounded by quotes.

```bash
# Single quotes
name = 'heloo'

# Double quotes
greeting = "Hello World"
#Both work the same.

#Numbers inside a string (still text)
number_text = "12345"

#Special symbols allowed
password = "@mypassword123!"

# Indexing
name = "Python"
print(name[0])  # P
print(name[1])  # y
print(name[2])  # t
print(name[5])  # n


```

| Code          | Meaning                                             |
| ------------- | --------------------------------------------------- |
| `x = "apple"` | string (text)                                       |
| `x = apple`   | ERROR — Python thinks apple is a variable, not text |


#### Common Python String Methods
```bash

# upper()
# Converts the entire string to uppercase.

text = "hello"
print(text.upper())   # Output: HELLO

# lower()
#Converts the entire string to lowercase.

text = "HELLO"
print(text.lower())   # Output: hello

# title()
#Capitalizes the first letter of every word.

text = "welcome to python"
print(text.title())   # Output: Welcome To Python

# capitalize()
#Capitalizes only the first letter of the string.

text = "python is fun"
print(text.capitalize())  # Output: Python is fun

#strip()
#Removes spaces at the start and end.

text = "   hello   "
print(text.strip())   # Output: hello

# replace()
#Replaces part of the string with another string.

text = "I love Java"
print(text.replace("Java", "Python"))
# Output: I love Python

#split()

# the string into a list based on a separator (default = space).
text = "apple banana mango"
print(text.split())  
# Output: ['apple', 'banana', 'mango']

#join()
#Joins list items into a string using a separator.

words = ['a', 'b', 'c']
print("-".join(words))
# Output: a-b-c

#find()

# Returns the index of the first occurrence of a substring.
# If not found → returns -1.

text = "hello world"
print(text.find("world"))  # Output: 6

#count()
#Counts how many times a substring appears.

text = "banana"
print(text.count("a"))  # Output: 3


```

#### Slicing
- extracting a part of a string using indexes.


```bash
text = "HELLO"
print(text[1:4])   # Output: ELL
print(text[:3])    # Output: HEL
print(text[2:])    # Output: LLO
```

#### Escape sequences
| Escape Sequence | Meaning          | Example Output                          |
| --------------- | ---------------- | --------------------------------------- |
| `\n`            | New line         | Moves text to the next line             |
| `\t`            | Tab (4–8 spaces) | Adds indentation                        |
| `\'`            | Single quote     | `'Hello'` inside single quotes          |
| `\"`            | Double quote     | `"Hello"` inside double quotes          |
| `\\`            | Backslash        | Prints a single `\`                     |
| `\r`            | Carriage return  | Moves cursor to beginning of line       |
| `\b`            | Backspace        | Removes one character                   |
| `\f`            | Form feed        | Page break (rarely used)                |
| `\a`            | Bell sound       | Makes system alert sound (if supported) |


```bash
print("Hello\nWorld")
# Output:
# Hello
# World

print("Name:\tAyush")
# Output:
# Name:    Ayush

print('It\'s a sunny day')
# Output:
# It's a sunny day

print("He said \"Python\"")
# Output:
# He said "Python"

print("C:\\Users\\Ayush")
# Output:
# C:\Users\Ayush

print("Hello World\rHi")
# Output (Hi replaces beginning):
# Hi World

print("Hellooo\b!")
# Output (backspace removes one 'o'):
# Helloo!

print("Hello\fWorld")
# Output (form feed moves text down):
# Hello
#       World

print("Beep\a")
# Output:
# (System bell sound, if supported)


```



####  Function
- A function in Python is a block of reusable code that performs a specific task.


- Syntax

```bash
def function_name(parameters):
    # code block
    return value

# define function
def add(a, b):
    return a + b
# Calling the function:
result = add(5, 3)
print(result)
# Output
8
```


#### Variable scope 
- where a variable can be accessed or used in your code.

- Local Scope

    - A variable created inside a function is local to that function.

    - you can use it only inside that function.
    - You cannot use it outside.

    - Example:
    ```bash
    def my_func():
        x = 10   # local variable
        print(x)

    my_func()
    print(x)   # Error: x is not defined
    ```
- Global Scope

    - A variable created outside all functions is global.

    - You can use it anywhere in the file (inside or outside functions).

    - Example:
    ```bash
    x = 20   # global variable

    def my_func():
        print(x)   # Works!

    my_func()
    print(x)       # Also works!
    ```


#### Comparison operators
- Comparison operators in Python are used to compare two values.
- They always return a Boolean value: True or False.

| Operator | Meaning                  | Example  | Output |
| -------- | ------------------------ | -------- | ------ |
| `==`     | Equal to                 | `5 == 5` | True   |
| `!=`     | Not equal to             | `5 != 3` | True   |
| `>`      | Greater than             | `7 > 3`  | True   |
| `<`      | Less than                | `2 < 5`  | True   |
| `>=`     | Greater than or equal to | `5 >= 5` | True   |
| `<=`     | Less than or equal to    | `3 <= 2` | False  |

```bash

x = 10
y = 5

print(x == y)   # False
print(x != y)   # True
print(x > y)    # True
print(x < y)    # False
print(x >= 10)  # True
print(y <= 2)   # False

```

#### Boolean Operators
| Operator | Meaning                          | Example          | Output |
| -------- | -------------------------------- | ---------------- | ------ |
| `and`    | True if **both** are True        | `True and False` | False  |
| `or`     | True if **at least one** is True | `True or False`  | True   |
| `not`    | **Reverses** the Boolean value   | `not True`       | False  |


```bash
x = 10
y = 5
print(x > 5 and y < 10)  # True and True -> True
print(x > 5 and y > 10)  # True and False -> False

x = 10
y = 5
print(x > 5 or y > 10)   # True or False -> True
print(x < 5 or y > 10)   # False or False -> False

```
#### conditional statements
- if Statement

    - Used to run code only if a condition is True.
    ```bash
        x = 10

        if x > 5:
            print("x is greater than 5")


        # Output:

        x is greater than 5
    ```
- if-else Statement
    - Runs one block if True, another block if False.
    ```bash
    x = 3

    if x > 5:
        print("x is greater than 5")
    else:
        print("x is 5 or less")


    # Output:

    x is 5 or less
    ```
    
    
- elif (else if) Statement

    - Used when you have multiple conditions.
    ```bash
    x = 7

    if x > 10:
        print("x is greater than 10")
    elif x > 5:
        print("x is greater than 5 but less than or equal to 10")
    else:
        print("x is 5 or less")


    # Output:

    x is greater than 5 but less than or equal to 10
    ```
- Nested if Statement

    - An if inside another if.
    ```bash
    x = 15

    if x > 10:
        print("x is greater than 10")
        if x % 2 == 0:
            print("x is also even")
        else:
            print("x is odd")


    # Output:

    x is greater than 10
    x is odd

    ```


#### Loops

- FOR Loop

    - Used to repeat a block of code for each item in a sequence (list, string, range, etc.).

    - Example:
    ```bash
    for i in range(1, 6):
        print(i)

    # Output:
    1
    2
    3
    4
    5
    ```
- WHILE Loop

    - Repeats a block of code as long as a condition is TRUE.

    - Example:
    ```bash
    count = 1
    while count <= 5:
        print(count)
        count += 1

    Output:
    1
    2
    3
    4
    5
    ```


####  list 

- A collection of multiple items stored in a single variable, written inside square brackets [].

```bash
my_list = [10, 20, 30, "apple", True]
print(my_list)


```

#### Indexing in List
- Accessing a single item using its index (position).

```bash
fruits = ["apple", "banana", "cherry", "mango"]

print(fruits[0])     # apple
print(fruits[1])     # banana
print(fruits[-1])    # mango   (last item)
print(fruits[-2])    # cherry
```

#### Slicing in List
-Extracting a part (range) of the list using [start:end]
(end index is NOT included).

```bash
fruits = ["apple", "banana", "cherry", "mango", "orange"]

print(fruits[1:4])     # ['banana', 'cherry', 'mango']
print(fruits[:3])      # ['apple', 'banana', 'cherry']
print(fruits[2:])      # ['cherry', 'mango', 'orange']
print(fruits[-3:])     # ['cherry', 'mango', 'orange']
print(fruits[0:5:2])   # ['apple', 'cherry', 'orange']   (step = 2)


```
#### del with List Indexing
- del is used to delete an item from a list using its index.
```bash

fruits = ["apple", "banana", "cherry", "mango", "orange"]

del fruits[1]      # deletes item at index 1 → "banana"
print(fruits)      # ['apple', 'cherry', 'mango', 'orange']

del fruits[-1]     # deletes last item → "orange"
print(fruits)      # ['apple', 'cherry', 'mango']


fruits = ["apple", "banana", "cherry", "mango", "orange", "kiwi"]

del fruits[1:4]      # deletes 'banana', 'cherry', 'mango'
print(fruits)        # ['apple', 'orange', 'kiwi']

del fruits[:2]       # deletes first two items
print(fruits)        # ['kiwi']



nums = [1, 2, 3]
del nums
# print(nums)   # ERROR: list is deleted

```

#### dictionary

- A collection of data stored in key–value pairs using {}.

```bash
person = {
    "name": "naman",
    "age": 25,
    "city": "Delhi"
}
print(person)
print(person["age"])


# output
{'name': 'naman', 'age': 25, 'city': 'Delhi'}
25



```
#### dict()


```bash
values = dict(a=1, b=2, c=3)
print(values)

output:
{'a': 1, 'b': 2, 'c': 3}

```

#### tuple

- An ordered, immutable (unchangeable) collection of items written inside parentheses ().

```bash
my_tuple = (10, 20, 30, "apple", True)
print(my_tuple)
# (10, 20, 30, 'apple', True)

my_tuple = ("a", "b", "c")
print(my_tuple[0])   # a
print(my_tuple[-1])  # c

nums = (1, 2, 3, 4, 5)
print(nums[1:4])   # (2, 3, 4)
print(nums[:3])    # (1, 2, 3)


```

#### sets

- A set is an unordered, unindexed, mutable collection of unique items, written using { }.
- Set = Collection of unique values (no duplicates allowed).

```bash
my_set = {10, 20, 30, 20, 10}
print(my_set)  
# {10, 20, 30}   (duplicates removed)

```

```bash
# Create initial sets
a = {1, 2, 3}
b = {3, 4, 5}

# 1. add()
a.add(4)
print("add:", a)  
# Output: {1, 2, 3, 4}

# 2. update()
a.update([5, 6])
print("update:", a)
# Output: {1, 2, 3, 4, 5, 6}

# 3. remove()
a.remove(6)
print("remove:", a)
# Output: {1, 2, 3, 4, 5}

# 4. discard()
a.discard(10)  # no error if 10 not in set
print("discard:", a)
# Output: {1, 2, 3, 4, 5}

# 5. pop()
value = a.pop()
print("pop removed:", value, "remaining:", a)
# Output: random removed value, remaining set varies

# 6. clear()
temp = {10, 20, 30}
temp.clear()
print("clear:", temp)
# Output: set()

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

# 7. union()
print("union:", a.union(b))
# Output: {1, 2, 3, 4, 5}

# 8. intersection()
print("intersection:", a.intersection(b))
# Output: {3}

# 9. difference()
print("difference:", a.difference(b))
# Output: {1, 2}

# 10. symmetric_difference()
print("symmetric_difference:", a.symmetric_difference(b))
# Output: {1, 2, 4, 5}

# 11. issubset()
print("issubset:", {1,2}.issubset(a))
# Output: True

# 12. issuperset()
print("issuperset:", a.issuperset({1}))
# Output: True

# 13. isdisjoint()
print("isdisjoint:", a.isdisjoint({10, 20}))
# Output: True
# n

````
