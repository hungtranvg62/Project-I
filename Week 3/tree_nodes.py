class TreeNode:
    def __init__(self, id):
        self.id = id
        self.children = []

class Tree:
    def __init__(self):
        self.nodes = {}
        self.root = None

    def make_root(self, id):
        if id in self.nodes:
            return
        self.root = TreeNode(id)
        self.nodes[id] = self.root

    def insert(self, u, v):
        if u in self.nodes or v not in self.nodes:
            return
        new_node = TreeNode(u)
        self.nodes[u] = new_node
        self.nodes[v].children.append(new_node)

    def pre_order(self, node, result):
        if not node:
            return
        result.append(node.id)
        for child in node.children:
            self.pre_order(child, result)

    def in_order(self, node, result):
        if not node:
            return
        if len(node.children) > 0:
            self.in_order(node.children[0], result)  # Thăm con trái (nếu có)
        result.append(node.id)  # Thăm gốc
        for i in range(1, len(node.children)):
            self.in_order(node.children[i], result)  # Thăm các con tiếp theo

    def post_order(self, node, result):
        if not node:
            return
        for child in node.children:
            self.post_order(child, result)
        result.append(node.id)

    def execute_command(self, command):
        cmd = command.split()
        if cmd[0] == "MakeRoot":
            self.make_root(int(cmd[1]))
        elif cmd[0] == "Insert":
            self.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "PreOrder":
            result = []
            self.pre_order(self.root, result)
            print(" ".join(map(str, result)))
        elif cmd[0] == "InOrder":
            result = []
            self.in_order(self.root, result)
            print(" ".join(map(str, result)))
        elif cmd[0] == "PostOrder":
            result = []
            self.post_order(self.root, result)
            print(" ".join(map(str, result)))

# Đọc dữ liệu đầu vào và thực hiện các lệnh
tree = Tree()

while True:
    command = input().strip()
    if command == '*':
        break
    tree.execute_command(command)
