my_list = [3, 2, 1, 4, 5]


def sort_part(alist, low_idx, pivot_idx):
    pivot_val = alist[pivot_idx]

    while pivot_idx != low_idx:
        low_val = alist[low_idx]

        print(alist, low_val, pivot_val)
        if low_val <= pivot_val:
            low_idx += 1
        else:
            alist[low_idx] = alist[pivot_idx - 1]
            alist[pivot_idx] = low_val
            alist[pivot_idx - 1] = pivot_val
            pivot_idx -= 1

    return pivot_idx


def quicksort(alist, low_idx, high_idx):
    if low_idx > high_idx:
        return

    pivot_idx = sort_part(alist, low_idx, high_idx)
    quicksort(alist, low_idx, pivot_idx-1)
    quicksort(alist, pivot_idx+1, high_idx)


quicksort(my_list, 0, len(my_list)-1)
print(my_list)


# sort_part(my_list, 0, 4)
