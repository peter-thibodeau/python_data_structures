def QuickSort(lst):
    item = len(lst)

    if item < 2: # not enough items to sort
        return lst

    pivot = 0

    for i in range(1, item):  # splitting
        if lst[i] <= lst[0]:
            pivot += 1
            temp = lst[i]
            lst[i] = lst[pivot]
            lst[pivot] = temp

    # swapping pivot with adjacent item
    temp = lst[0]
    lst[0] = lst[pivot]
    lst[pivot] = temp

    left = QuickSort(lst[0:pivot])  # Sort left of pivot
    right = QuickSort(lst[pivot + 1:item])  # sort right of pivot

    lst = left + [lst[pivot]] + right  # re-assemble the parts

    return lst

if __name__ == "__main__":
    lst = [64, 34, 25, -12, 22, 11, 90]

print("Original list: ", lst)
print("Sorted list: ", QuickSort(lst))

# ANSWER The time complexity of the quick sort = O(n log(n))