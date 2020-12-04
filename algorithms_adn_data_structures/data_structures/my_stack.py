# Custom implementation of stack


class MyStack:
    def __init__(self):
        self.__stack = []

    def push(self, x):
        self.__stack.append(x)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty, bitch!")
        return self.__stack.pop()

    def top(self):
        return self.__stack[-1]

    def clear(self):
        self.__stack.clear()

    def is_empty(self):
        return len(self.__stack) == 0

    def get_size(self):
        return len(self.__stack)
