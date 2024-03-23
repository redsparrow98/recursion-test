# Please refer to the README.txt for program desc

#================   function    ==============================

def adding_up_to(int_list, index_num):
    """This function is a recursive function. it takes a list argument and a int index
    argument. if the index is lesser or equal to 0 it returns the first item in
    the list as the sum. this is the base case.
    
    otherwise it finds the index item in the list and adds on to it by calling on the
    adding_up_to function again using the same constant list as the argument but this time
    the initial index is deducted by 1.
    
    it keeps calling on to itself until the index reaches the 0 and once all the function
    calls are returned it adds up going back to the original call.
    
    finally returns the sum of all the items in the list up to and including the original
    index point provided.
    
    Args:
        int_list (_type_: list): a list of integers
        index (_type_: int): a single integer
        
    Returns:
        integer: returns the sum of all the numbers up to and including the index
        point for the function in the list.
    """
    # base case if index is 0 or less returns the first item
    if index_num <= 0:
        return int_list[0]
    # recursion- add the current element to the sum of the rest of the list
    # the index number is deducted by 1 every time the func is called
    else:
        return int_list[index_num] + adding_up_to(int_list, index_num - 1)

#================   final code  ===========================

# Example usage:
num_list = [1, 12, 2, 38, 3, 14, 4, 26, 6, 7, 8, 5, 9, 10]
print(f"This is the list: \n{list}")

# set up a loop to ask for index number if index is out of range for the list
# it keeps asking for the index within range of the list
wrong_input = True
while wrong_input:
    index = int(input("\nWhat index number would you like? (0 to 13): "))
    if index > len(num_list) - 1:
        print("Sorry the list isn't that long try another index.")
    else:
        wrong_input = False
        result = adding_up_to(num_list, index)
        print(f"The sum up to index {index} is: {result}")
