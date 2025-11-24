"""

you will print 10 descending integers starting from 10 and ending at 1 with each integer being 1 less than the last and each integer printed on a new line.

Create a variable and assign it the integer 10.

Then, print

10

9

8

7

6

5

4

3

2

1

in the output by using a while loop to print numbers while the variable does not equal 0.  Use the -= operator to reassign descending values to the variable.
"""
dec_int = 10
 
while dec_int != 0:
    print(dec_int)
    dec_int -= 1