"""
Create a variable and assign it a list that contains an integer, a float, a Boolean value, a string, and a list of 3 integers.

Create another variable and assign it a call of the list() function with a string as its argument.

Use the keyword "in" to check if the letter "e" is in the list assigned to the variable from step 2 and print the result.

Use the keyword "not in" to check if the letter "a" is not in the list assigned to the variable from step 2 and print the result.
"""


mixed = [10, 4.97, True, "mountain", [9, 8, 7]]
li_str = list("cheese")
print("e" in li_str)
print("a" not in li_str)



""""
Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]

Access the first list from the list of lists in step 1 by index then print it.

Access the 14 from the list in step 1 then print it.

Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]

Use a negative integer to access "chair" from the variable in step 4 by index then print it.

Print "Most people own at least 2 chairs." by concatenating the 2 from the list in step 1 and the "chair" from the list in step 4 with "Most people own at least ", a space, and a period.

Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]

Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7.

Print the slice [8.76, 6.54] from the variable you created in step 7.

Print the slice [0.98, 8.76] from the variable you created in step 7.

"""

up_by_two = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(up_by_two[0])
print(up_by_two[3][1])
furniture = ["chair", "table", "desk", "lamp", "bed"]
print(furniture[-5])
print("Most people own at least " + str(up_by_two[0][1]) + " " + furniture[0] + "s.")
floats = [0.98, 8.76, 6.54, 4.32]
print(floats[1:])
print(floats[1:3])
print(floats[:2])