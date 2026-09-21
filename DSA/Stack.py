# # s = []
# # s.append('https://www.cnn.com/')
# # s.append('https://www.cnn.com/world')
# # s.append('https://www.cnn.com/india')
# # s.append('https://www.cnn.com/china')
#
# # from collections import deque
# # stack = deque()
# #
# # stack.append('https://www.cnn.com/')
# # stack.append('https://www.cnn.com/world')
# # stack.append('https://www.cnn.com/india')
# # stack.append('https://www.cnn.com/china')
# # print(stack)
# # # stack.pop()
# # # print(stack)
#
# # -----------------------------------------------------------------
# # Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# # reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
#
# from collections import deque
#
#
# class Stack:
#     def __init__(self):
#         self.container = deque()
#
#     def push(self, value):
#         self.container.append(value)
#
#     def pop(self):
#         return self.container.pop()
#
#     def peek(self):
#         return self.container[-1]
#
#     def is_empty(self):
#         return len(self.container) == 0
#
#     def size(self):
#         return len(self.container)
#
#
# def reverse_string(text):
#     s = Stack()
#     rev_text = " "
#     i = 0
#     for char in text:
#         s.push(char)
#         # print(self.container)
#     while s.size() != 0:
#         rev_text += s.pop()
#     return rev_text
#
#
# print(reverse_string("We will conquere COVID-19"))
# print(reverse_string("malayalam"))
#
# # Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def is_match(c1, c2):
    match_set = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    return match_set[c1] == c2


def is_balanced(inp):
    s = Stack()
    for char in inp:
        if char == '(' or char == '{' or char == '[':
            s.push(char)
        if char == ')' or char == '}' or char == ']':
            if s.size() == 0:
                return False
            if not is_match(char,s.pop()):
                return False

    return s.size() == 0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
