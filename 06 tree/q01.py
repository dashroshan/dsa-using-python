"""
Question at : https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree_exercise.md
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, type, level=0):
        if type == "name":
            dataContent = self.data["name"]
        elif type == "designation":
            dataContent = self.data["pos"]
        elif type == "both":
            dataContent = f"{self.data['name']} ({self.data['pos']})"
        print(f"{'   '*level}{'|__' if level!=0 else ''}{dataContent}")
        if self.children:
            for child in self.children:
                child.print_tree(type, level + 1)


def build_management_tree():
    ceo = TreeNode({"name": "Nilupul", "pos": "CEO"})

    cto = TreeNode({"name": "Chinmay", "pos": "CTO"})
    infra = TreeNode({"name": "Vishwa", "pos": "Infrastructure Head"})
    infra.addChild(TreeNode({"name": "Dhaval", "pos": "Cloud Manager"}))
    infra.addChild(TreeNode({"name": "Abhijit", "pos": "App Manager"}))
    app = TreeNode({"name": "Amir", "pos": "Application Head"})
    cto.addChild(infra)
    cto.addChild(app)

    hrHead = TreeNode({"name": "Gels", "pos": "HR Head"})
    hrHead.addChild(TreeNode({"name": "Peter", "pos": "Recruitment Manager"}))
    hrHead.addChild(TreeNode({"name": "Waqas", "pos": "Policy Manager"}))

    ceo.addChild(cto)
    ceo.addChild(cto)
    ceo.addChild(hrHead)

    return ceo


if __name__ == "__main__":
    root_node = build_management_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    root_node.print_tree("designation")  # prints only designation hierarchy
    root_node.print_tree("both")  # prints both (name and designation) hierarchy
