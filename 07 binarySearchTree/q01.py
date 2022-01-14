"""
Add following methods to BinarySearchTreeNode class created in main video tutorial

1. find_min(): finds minimum element in entire binary tree
2. find_max(): finds maximum element in entire binary tree
3. calculate_sum(): calcualtes sum of all elements
4. post_order_traversal(): performs post order traversal of a binary tree
5. pre_order_traversal(): perofrms pre order traversal of a binary tree
"""


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

    def pre_order_traversal(self):
        elements = []

        # visit base node
        elements.append(self.data)

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        # visit base node
        elements.append(self.data)

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

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        sum = 0
        sum += self.data
        if self.left:
            sum += self.left.calculate_sum()
        if self.right:
            sum += self.right.calculate_sum()
        return sum


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for element in elements[1:]:
        root.add_child(element)
    return root


if __name__ == "__main__":
    elements = [11, 2, 30, 4, 5]
    bst = build_tree(elements)
    print(f"In order Traversal={bst.in_order_traversal()} # left -> center -> right")
    print(f"Pre order Traversal={bst.pre_order_traversal()} # center -> left -> right")
    print(
        f"Post order Traversal={bst.post_order_traversal()} # left -> right -> center"
    )
    print(bst.search(4))
    print(f"Min={bst.find_min()} and Max={bst.find_max()}")
    print(f"Sum = {bst.calculate_sum()}")
