class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return self.value

class BinaryTree:

    def __init__(self):
        self.root = None

    def add_node(self, value):
        if not self.root:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if current.value > value:
                if current.left:
                    current = current.left
                    continue
                else:
                    current.left = Node(value)
                    break
            elif current.value < value:
                if current.right:
                    current = current.right
                    continue
                else:
                    current.right = Node(value)
                    break
            else:
                raise ValueError("Node already exists")

if __name__ == "__main__":
    tree = BinaryTree()
    tree.add_node(9)
    tree.add_node(8)
    tree.add_node(7)
    tree.add_node(15)