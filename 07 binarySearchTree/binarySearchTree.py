import mimetypes


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for element in elements[1:]:
        root.add_child(element)
    return root


if __name__ == "__main__":
    elements = [1, 2, 3, 4, 5]
    bst = build_tree(elements)
    bst.delete(4)
    print(bst.in_order_traversal())
