import multiprocessing
import time


def calculate_square(n):
    for i in n:
        print(f'Square: {i * i}')


def calculate_cube(n):
    for i in n:
        print(f'Cube: {i * i * i}')

if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]

    p1 = multiprocessing.Process(target=calculate_square, args=(arr,))
    p2 = multiprocessing.Process(target=calculate_cube, args=(arr,))


    p1.start()
    p2.start()

    p1.join()
    p2.join()
