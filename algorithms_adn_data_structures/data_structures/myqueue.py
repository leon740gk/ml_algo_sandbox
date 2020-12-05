from collections import deque


class MyQueue:

    def __init__(self):
        self.__buffer = deque()

    def enqueue(self, value):
        self.__buffer.appendleft(value)

    def dequeue(self):
        return self.__buffer.pop()

    def is_empty(self):
        return len(self.__buffer) == 0

    def size(self):
        return len(self.__buffer)
