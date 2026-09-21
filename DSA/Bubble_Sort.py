#
# def BubbleSort(elements):
#     size = len(elements)
#
#     for i in range(size-1):
#         swapped = False
#         for j in range(size-1-i):
#             if elements[j] > elements[j+1]:
#                 temp = elements[j]
#                 elements[j] = elements[j+1]
#                 elements[j+1] = temp
#                 swapped = True
#
#         if not swapped:
#             break
#
# if __name__ == '__main__':
#     elements = [5, 9, 2, 1, 67, 34, 88, 34]
#     # elements = [1, 2, 3, 4]
#     BubbleSort(elements)
#     print(elements)

# ---------------------------------------------------------------------------

def Bubble_Sort(elements, Key):
    size = len(elements)

    for i in range(size - 1):  # iterates 3 times to get sorted
        swapped = False
        for j in range(size - 1-i):  # iterates through each key-value pair, j -> key-value pair
            if elements[j][Key] > elements[j + 1][Key]:
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    Bubble_Sort(elements, 'name')
    print(elements)
