list = [101, 44, 62, 3, 7, 74]


def bubblesort(list):
    high_idx = len(list) - 1

    for i in range(high_idx):
        list_changed = False
        for j in range(high_idx):
            item = list[j]
            next = list[j+1]

            if item > next:
                list[j] = next
                list[j+1] = item
                list_changed = True

            print(list, i, j)
        print(list_changed)
        if list_changed == False:
            break


bubblesort(list)
