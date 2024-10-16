"""
The Merge Sort algorithm works this way:
    1.	Subdivide the array at the pivot, each sub-array should be half as big as the original.
    2.	Continue to subdivide if the current sub-array has more than one element.
    3.	Sort the sub-arrays.
    4.  Merge two sub-arrays together.
    5.	Repeat until there are no more sub-arrays.
"""

def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    # subdivide
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # continue with recursion
    left_sort = mergeSort(left)
    right_sort = mergeSort(right)

    return actually_do_it(left_sort, right_sort) # do the actual sorting and merging

def actually_do_it(left, right):
    result = []
    i = j = 0

    # sorting
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # merging
    result.extend(left[i:])
    result.extend(right[j:])

    return result

if __name__ == "__main__":
    lst = ['banana', 'apple', 'raisin', 'cherry']
    print("Original list: ", lst)
    print("Sorted list: ", mergeSort(lst))

