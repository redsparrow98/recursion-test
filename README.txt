===================    sum_recursion    ===================
### Function
Creates a recursion function add_up_to(int_list, index)
takes a list of integers and a index number. sums up all the
numbers in the list up to and including the index number

teh base case for the function is the index if it 0 or less
then it just returns te first item in the list

otherwise it finds the index item in the list and adds the return
of the add_up_to function again but this time the index in the
recursion is reduced by 1.
it keeps looping trough this part until the index reaches 0 in which
case it returns the first item in the list.
the recursion ends at this point and the else statement for each recursion
goes backwards adding up the totals of all the returns

Args:
    int_list (_type_: list): a list of integers
    index (_type_: int): a single integer
Returns:
    integer: returns the sum of all the numbers up to and including the
    index point for the function in the list.

### final code

in the final code it provides the print of the list for comparison

sets up a while loop to request user input for the index if the index input
is outside of the list range it keeps asking

once the index input is within the range it passes the list and that
index in to the adding_up_to function and ends the while loop

finally prints out the sum of all the numbers in list for the
provided index

===================    largest_number    ===================
### Function
Creates a recursion function largest_number(list)
takes a list of integers and finds the largest number in the list

the base case for this function is the list length being 1 item looping
in which case it returns the only item in the list

otherwise compares the 1st item in list to the largest number from the
list thats sliced from 1st item. it keeps slicing the 1st item until the list gets
to be only 1 item and it reaches base case after reaching base case it goes up the 
recursion again and compares the 1st item to the return of the function passing on
the max to the next return until we reach the initial call. (start of the recursion)

 Args:
    list (list): a list of integer numbers
Returns:
    integer: returns the largest value in the input list

### final code

provides a list and prints it out for comparison and checking

calls on to the function largest_number and passes the provided list