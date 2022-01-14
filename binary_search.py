def binary_search(list, target):
    """
    """
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2

        if(list[midpoint] == target):
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


if __name__ == "__main__":
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    index = binary_search(number_list, 1)
    print("INDEX=", index, "TARGET=", number_list[index])
