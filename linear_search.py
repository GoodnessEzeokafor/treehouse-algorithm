def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None



if __name__ == '__main__':
    number_list = [1,2,3,4,5]
    index = linear_search(number_list, 5)
    print("INDEX=", index, "TARGET=",number_list[index])
