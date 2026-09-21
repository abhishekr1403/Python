#
# def sum(list):
#     if len(list) == 1:
#         return list[0]
#     else:
#         return list[0] + sum(list[1:])
#
# list_num = [1,2,3,4,5]
# print(sum(list_num))

# def recursive_sum_list(data):
#     total = 0
#     for element in data:
#         if type(element) == type([]):
#             total = total + recursive_sum_list(element)
#         else:
#             total = total + element
#     return total
#
# print(recursive_sum_list([1, 2, [3, 4], [5, 6]]))

# def fact(n):
#     if n <= 0:
#         return  None
#     elif n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
# print(fact(0))

# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
# print(fib(6))

# def sumDigits(n):
#     if n == 0:
#         return 0
#     else:
#         s = n % 10
#         s = s + sumDigits(int(n / 10))
#         return s
#
#
# print(sumDigits(124))

# def power(a,b):
#     if a== 0:
#         return 0
#     elif b== 0:
#         return 1
#     else:
#         return a * power(a, b-1)
# print(power(5,2))
