# numbers_set = {1, 2, 3, 4, 4}
# numbers_set = {1, 2, 3, 4, 4} #duplicate vals removed
# numbers_set = {1, 2, 3, 4, (5, 6)} #tuples can be used in sets but not lists
# print(numbers_set)

words_set = {"Alpha", "Bravo", "Charlie"}
# abcd = ""
# for word in words_set:  ##Example of concatenation##
# abcd += word  ##Sets unordered, no numerical index##
# print(abcd)
# if "Alpha" in words_set:
# print("Alpha is in set")
# else:
# print("Alpha is not in set")  ##can check in despite no index##

words_set.add("Delta")
print(words_set)
words_set.discard("Bravo")
print(words_set)
