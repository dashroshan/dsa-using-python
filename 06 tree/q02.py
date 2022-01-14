"""
Question at : https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, uptoLevel, level=0):
        if level > uptoLevel:
            return
        print(f"{'   '*level}{'|__' if level!=0 else ''}{self.data}")
        if self.children:
            for child in self.children:
                child.print_tree(uptoLevel, level + 1)


def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == "__main__":
    root_node = build_location_tree()
    root_node.print_tree(1)
    root_node.print_tree(2)
    root_node.print_tree(3)
