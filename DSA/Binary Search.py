from operator import index


def binary_search(num_list, item):
    left_index = 0
    mid_index = 0
    right_index = len(num_list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_num = num_list[mid_index]

        if mid_num == item:
            return mid_index

        if mid_num < item:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def find_all_occurances(num_list, item):
    index = binary_search(num_list, item)
    indices = [index]

    # for lhs
    i = index - 1
    while i >= 0:
        if num_list[i] == item:
            indices.append(i)
        else:
            break
        i = i - 1

        # for rhs
        i = index + 1
        while i < len(num_list):
            if num_list[i] == item:
                indices.append(i)
            else:
                break
            i = i + 1

    return sorted(indices)

def recursive_binary_search(num_list, item, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    # if mid_index >= len(num_list) or mid_index < 0:
    #     return -1

    mid_num = num_list[mid_index]

    if mid_num == item:
        return mid_index

    if mid_num < item:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return recursive_binary_search(num_list, item, left_index, right_index)


if __name__ == '__main__':
    numbers = [1, 4, 6, 9, 10, 5, 7]
    number_to_find = 5
    # numbers.sort()

    # index = binary_search(numbers, number_to_find)
    # print(f"Number found at index {index} using binary search")
    #     indx = recursive_binary_search(numbers, number_to_find,0,len(numbers)-1)
    #     print(f"Number found at index {indx} using Recursive binary search")

    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 4
    indices = find_all_occurances(numbers, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")
