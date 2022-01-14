class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def printTree(self, level=0):
        print(f"{'   '*level}{'|__' if level!=0 else ''}{self.data}")
        if self.children:
            for child in self.children:
                child.printTree(level + 1)


def createTree():
    root = TreeNode("Students")

    cse = TreeNode("CSE")
    cse.addChild(TreeNode("Name1"))
    cse.addChild(TreeNode("Name2"))

    it = TreeNode("IT")
    it.addChild(TreeNode("Name1"))
    it.addChild(TreeNode("Name2"))

    root.addChild(cse)
    root.addChild(it)

    return root


if __name__ == "__main__":
    data = createTree()
    data.printTree()
    pass
