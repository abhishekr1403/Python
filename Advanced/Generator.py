def sqaure():
    a = 1
    while True:
        yield a ** 2
        a += 1

for n in sqaure():
    if n > 20:
        break
    print(n)