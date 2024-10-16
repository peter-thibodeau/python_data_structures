"""
The Merge Sort algorithm works this way:
    1.	Subdivide the array two around the pivot, each sub-array should be half as big as the original.
    2.	Continue to subdivide if the current sub-array has more than one element.
    3.	Sort and merge two sub-arrays together.
    4.	Repeat until there are no more sub-arrays.
"""

def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    # subdivide
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # continue by using recursion
    left_sort = mergeSort(left)
    right_sort = mergeSort(right)

    return merge(left_sort, right_sort) # get them sorted

def merge(left, right): # sorting
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:]) # add smaller items before pivot
    result.extend(right[j:]) # add larger items after pivot

    return result

if __name__ == "__main__":
    lst = ['banana', 'apple', 'raisin', 'cherry']
    merged_lst = mergeSort(lst)
    print("Sorted lstay:", merged_lst)


