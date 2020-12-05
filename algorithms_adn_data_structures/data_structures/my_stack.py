# Custom implementation of stack
# List and Deque
from collections import deque


class StackList:
    def __init__(self):
        self.__stack = []

    def push(self, x):
        self.__stack.append(x)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.__stack.pop()

    def top(self):
        return self.__stack[-1]

    def clear(self):
        self.__stack.clear()

    def is_empty(self):
        return len(self.__stack) == 0

    def get_size(self):
        return len(self.__stack)


class StackDeque:
    def __init__(self):
        self.__container = deque()

    def push(self, value):
        self.__container.append(value)

    def pop(self):
        return self.__container.pop()

    def peek(self):
        return self.__container[-1]

    def is_empty(self):
        return len(self.__container) == 0

    def size(self):
        return len(self.__container)
