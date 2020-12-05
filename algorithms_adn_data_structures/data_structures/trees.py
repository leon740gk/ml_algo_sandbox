from typing import List


class TreeNode:
    """
    General Tree structure
    https://www.youtube.com/watch?v=4r_XR9fUPhQ&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=9
    """
    def __init__(self, data):
        self._data = data
        self._children = []
        self._parent = None
        self._level = 0

    def _set_parent(self, parent):
        self._parent = parent

    def _set_level(self, level):
        self._level = level

    def add_child(self, child):
        child._set_parent(self)
        child._set_level(child._level + 1)
        if child._children:
            for cld in child._children:
                cld._set_level(cld._level + 1)
        self._children.append(child)

    def get_node_level(self):
        return self._level

    def print_tree(self):
        level_ident = ">"
        if self._parent:
            level_ident = "--" * self._level * 2 + ">"
        print(f"{level_ident} {self._data}")
        if self._children:
            for child in self._children:
                child.print_tree()


class BinarySearchTreeNode:
    """
    Binary Search Tree (BST)
    It can be used for sorting arrays and remove duplicates
    https://www.youtube.com/watch?v=lFq5mYUWEBk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=10
    https://www.youtube.com/watch?v=JnrbMQyGLiU&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=11
    """

    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def add_child(self, data):
        if data == self._data:
            return
        if data < self._data:
            if self._left:
                self._left.add_child(data)
            else:
                self._left = BinarySearchTreeNode(data)
        else:
            if self._right:
                self._right.add_child(data)
            else:
                self._right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # first visit left tree
        if self._left:
            elements += self._left.in_order_traversal()

        # then visit node itself
        elements.append(self._data)

        # last visit right tree
        if self._right:
            elements += self._right.in_order_traversal()

        return elements

    def search(self, value):
        if value == self._data:
            return True
        if value < self._data:
            if self._left:
                return self._left.search(value)
            else:
                return False
        else:
            if self._right:
                return self._right.search(value)
            else:
                return False

    def find_max(self):
        if self._right is None:
            return self._data
        return self._right.find_max()

    def find_min(self):
        if self._left is None:
            return self._data
        return self._left.find_min()

    def delete(self, value):
        if value < self._data:
            if self._left:
                self._left = self._left.delete(value)
        elif value > self._data:
            if self._right:
                self._right = self._right.delete(value)
        else:
            if self._left is None and self._right is None:
                return None
            if self._left is None:
                return self._right
            if self._right is None:
                return self._left

            min_value_of_right = self._right.find_min()
            self._data = min_value_of_right
            self._right = self._right.delete(min_value_of_right)

        return self


def build_bst(elements: List) -> BinarySearchTreeNode:
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


def build_test_tree() -> TreeNode:
    root = TreeNode("Emperor")

    morty = TreeNode("Morty")
    morty.add_child(TreeNode("Azazel"))
    morty.add_child(TreeNode("Ismail"))
    morty.add_child(TreeNode("Izrael"))

    horus = TreeNode("Horus")
    horus.add_child(TreeNode("Alex"))
    horus.add_child(TreeNode("Gregor"))
    horus.add_child(TreeNode("Gideon"))

    alfa_omega = TreeNode("Alfa")
    alfa_omega.add_child(TreeNode("Zero"))
    alfa_omega.add_child(TreeNode("Lightning"))
    alfa_omega.add_child(TreeNode("Flow"))

    root.add_child(morty)
    root.add_child(horus)
    root.add_child(alfa_omega)

    return root


if __name__ == "__main__":

    general_tree_root = build_test_tree()
    general_tree_root.print_tree()

    elements_for_bst = [13, 4, 7, 24, 46, 12, 11, 76, 3, 4, 7, 47]
    bst_root_numbers = build_bst(elements_for_bst)
    print(bst_root_numbers._data)
    print(bst_root_numbers.in_order_traversal())
    bst_root_numbers.delete(12)
    print(bst_root_numbers.in_order_traversal())

    names_for_bst = ["Alex", "Zena", "Gregor", "Gideon", "Tris", "Jeniffer", "Yu"]
    bst_root_names = build_bst(names_for_bst)
    print(f"Is Tris in this Tree? --> {bst_root_names.search('Tris')}")
    print(f"Is Tris in this Saber? --> {bst_root_names.search('Saber')}")
    print(bst_root_names.in_order_traversal())
