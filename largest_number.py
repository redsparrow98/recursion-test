# Please refer to the README.txt for program desc
#================   function    ==============================

def larges_number(int_list):
    """This function takes a list as input and checks the base case if the list only has
    1 item in it it returns that item as the largest one.
    
    If however the list has more than 1 items then it compares the max of the 1st item in
    teh list to the max of the rest of the list excluding the 1st item. and returns the
    larger number.

    Args:
        list (list): a list of integer numbers

    Returns:
        integer: returns the largest value in the input list
    """
    # base case: if the list only has 1 item that would be the largest number
    if len(int_list) == 1:
        return int_list[0]
    # recursion: compares the 1st item in list to the largest number from the
    # list thats sliced that 1st item. it keeps slicing the 1st item until the list gets
    # to be only 1 item and it reaches base case.
    # after reaching base case it goes up the recursion again and compares the 1st
    # item to the return of the function passing on the max to the
    # next return until we reach the initial call. (start of the recursion)
    else:
        return max(int_list[0], larges_number(int_list[1:]))

#================   final code  ===========================

my_list = [1, 5, 9, 2, 8, 3, 7]
print(my_list)
print(f"\nThe largest number is: {larges_number(my_list)}")
