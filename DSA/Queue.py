# # from collections import deque
# # class Queue:
# #     def __init__(self):
# #         self.buffer = deque()
# #     def enqueue(self,value):
# #         self.buffer.appendleft(value)
# #     def dequeue(self):
# #         return self.buffer.pop()
# #     def is_Empty(self):
# #         return len(self.buffer) == 0
# #     def size(self):
# #         return len(self.buffer)
# #
# # if __name__ == '__main__':
# #     pq = Queue()
# #     pq.enqueue({
# #         'company': 'Wall Mart',
# #         'timestamp': '15 apr, 11.01 AM',
# #         'price': 131.10
# #     })
# #     pq.enqueue({
# #         'company': 'Wall Mart',
# #         'timestamp': '15 apr, 11.02 AM',
# #         'price': 135.30
# #     })
# #     pq.enqueue({
# #         'company': 'Wall Mart',
# #         'timestamp': '15 apr, 11.03 AM',
# #         'price': 141.50
# #     })
# #     print(pq.buffer)
# #     print(pq.size())
# #     print(pq.is_Empty())
# #
# # -------------------------------------------------------------------------------------------------------
#
# Design a food ordering system where your python program will run two threads,
#
# Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
# Use this video to get yourself familiar with multithreading in python
#
# Pass following list as an argument to place order thread,
#
# orders = ['pizza','samosa','pasta','biryani','burger']
# This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.

# import time
# import threading
# from collections import deque
#
#
# class Queue:
#     def __init__(self):
#         self.buffer = deque()
#
#     def enqueue(self, value):
#         self.buffer.appendleft(value)
#
#     def dequeue(self):
#         if len(self.buffer) == 0:
#             print("The Queue is empty!")
#             return
#
#         return self.buffer.pop()
#
#     def is_Empty(self):
#         return len(self.buffer) == 0
#
#     def size(self):
#         return len(self.buffer)
#
# q = Queue()
# def place_order(orders):
#     for item in orders:
#         q.enqueue(item)
#         time.sleep(0.5)
#         # print(q.buffer)
#
#
# def serve_order():
#     time.sleep(1)
#     while q.buffer:
#         serve = q.dequeue()
#         print(f'The {serve} order is ready to serve..!')
#         time.sleep(2)
#     if not q.buffer:
#         print("The Queue is empty.")
# if __name__ == '__main__':
#
#     orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
#     t = time.time()
#
#     t1 = threading.Thread(target=place_order, args=(orders, ))
#     t2 = threading.Thread(target=serve_order,args=())
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print(time.time() - t)

# -----------------------------------------------------------------------------------------------------

from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("The Queue is empty!")
            return
        return self.buffer.pop()

    def is_Empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

def generate_binary(n):
    q = Queue()
    q.enqueue("1")

    for i in range(n):
        front = q.front()
        print(front)

        q.enqueue(front + "0")
        q.enqueue(front + "1")

        q.dequeue()

if __name__ == '__main__':
    generate_binary(10)