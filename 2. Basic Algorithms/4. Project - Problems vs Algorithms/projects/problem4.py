def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    i = 0
    i0 = 0
    i2 = len(input_list) - 1

    while i <= i2:
        if input_list[i] == 0:
            input_list[i], input_list[i0] = input_list[i0], 0
            i0 += 1
            i += 1

        elif input_list[i] == 2:
            input_list[i], input_list[i2]= input_list[i2], 2
            i2 -= 1

        else:
            i += 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Test Case 1 #######################################################
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print("TEST1_DONE\n")

# Test Case 2 #######################################################
test_function([0, 1, 1, 0, 1]) # List not includes 2
test_function([2, 1, 1, 2, 1]) # List not includes 0
print("TEST2_DONE\n")

# Test Case 2 #######################################################
test_function([])
print("TEST3_DONE\n")