def bubbleSort(lst):
    n = len(lst)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1): # do for each item to the right in the list

            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j] # swap with item on right if it's larger
                swapped = True

        if (swapped == False): # no items to the right are larger
            break


if __name__ == "__main__":
    lst = [64, 34, 25, -12, 22, 11, 90]

    bubbleSort(lst)

    print("Sorted list:")
    for i in range(len(lst)):
        print("%d" % lst[i], end=" ")