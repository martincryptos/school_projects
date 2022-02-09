def linear_search_dict(dict, target):
    for x, y in dict.items():
        if y == target:
            print("found at key: ", x)
            return y

    print("target not in dictionary")
    return -1


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dict(my_dictionary, 5)
linear_search_dict(my_dictionary, 3)
linear_search_dict(my_dictionary, 8)
