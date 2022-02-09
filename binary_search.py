def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_val = the_list[pivot]

        if pivot_val == target:
            print("computer got it!")
            return pivot
        if pivot_val > target:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1

    return -1


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(binary_search(my_list, 10))
# print(binary_search(my_list, 2))
# print(binary_search(my_list, 12))
