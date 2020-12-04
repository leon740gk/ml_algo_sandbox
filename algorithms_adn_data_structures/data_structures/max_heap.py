# Python3 implementation of Max Heap
# https://www.youtube.com/watch?v=g9YK6sftDi0
import sys


class MaxHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    @staticmethod
    def parent(pos):

        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    @staticmethod
    def left_child(pos):

        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def right_child(self, pos):

        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def is_leaf(self, pos):

        if (self.size // 2) <= pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, s_pos):

        self.Heap[fpos], self.Heap[s_pos] = (self.Heap[s_pos],
                                             self.Heap[fpos])

    # Function to heapify the node at pos
    def max_heapify(self, pos):

        # If the node is a non-leaf node and smaller
        # than any of its child
        if not self.is_leaf(pos):
            if (self.Heap[pos] < self.Heap[self.left_child(pos)] or
                    self.Heap[pos] < self.Heap[self.right_child(pos)]):

                # Swap with the left child and heapify
                # the left child
                if (self.Heap[self.left_child(pos)] >
                        self.Heap[self.right_child(pos)]):
                    self.swap(pos, self.left_child(pos))
                    self.max_heapify(self.left_child(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.right_child(pos))
                    self.max_heapify(self.right_child(pos))

    # Function to insert a node into the heap
    def insert(self, element):

        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] >
               self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Function to print the contents of the heap
    def print_it(self):

        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) +
                  " LEFT CHILD : " + str(self.Heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

    # Function to remove and return the maximum
    # element from the heap
    def extract_max(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.max_heapify(self.FRONT)

        return popped


if __name__ == "__main__":
    print('The maxHeap is ')

    maxHeap = MaxHeap(15)
    maxHeap.insert(5)
    maxHeap.insert(3)
    maxHeap.insert(17)
    maxHeap.insert(10)
    maxHeap.insert(84)
    maxHeap.insert(19)
    maxHeap.insert(6)
    maxHeap.insert(22)
    maxHeap.insert(9)

    maxHeap.print_it()

    print("The Max val is " + str(maxHeap.extract_max()))
