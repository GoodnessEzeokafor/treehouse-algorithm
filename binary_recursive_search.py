def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


if __name__ == "__main__":
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(recursive_binary_search(number_list, 3))
    # index = recursive_binary_search(number_list, 1)
    # print("INDEX=", index, "TARGET=", number_list[index])
