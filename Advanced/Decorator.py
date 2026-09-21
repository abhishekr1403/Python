def check(func):
    def helper(x):
        if type(x) == int and x > 0:
            return func(x)
        else:
            raise Exception("Argument is not a non-negative integer")

    return helper


@check
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        fact = n * factorial(n - 1)
    return fact


# for i in range(1, 10):
    # print(i, factorial(i))

# try:
#     print(factorial(-1))
# except Exception as e:
#     print(e)

try:
    print(factorial(1.354))
except Exception as e:
    print(e)