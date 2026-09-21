import threading
import time
from threading import Thread

#
# def calculate_square(n):
#     for i in n:
#         time.sleep(0.5)
#         print(f'Square: {i * i}')
#
#
# def calculate_cube(n):
#     for i in n:
#         time.sleep(0.5)
#         print(f'Cube: {i * i * i}')
#
# arr = [1, 2, 3, 4, 5]

# t1 = threading.Thread(target=calculate_square, args=(arr,))
# t2 = threading.Thread(target=calculate_cube, args=(arr,))
#
# t = time.time()
#
# # Using Multithreading
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# #Normal Case:
# # calculate_square(arr)
# # calculate_cube(arr)
#
# print(f'Time taken to execute is: {time.time() - t}')

# ----------------------------------------------------------------------

def sleepMe(i):
    print("Thread %i will sleep." % i)
    time.sleep(5)
    print("Thread %i is awake" % i)

for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
    print("Current Threads: %i." % threading.active_count())