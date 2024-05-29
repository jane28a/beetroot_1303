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

    def find_recursive(self, value, node=Ellipsis):
        if node is Ellipsis:
            node = self.root
        if node is None:
            return False
        if node.value < value:
            return self.find_recursive(value, node.right)
        elif node.value > value:
            return self.find_recursive(value, node.left)
        else:
            return True

    def find(self, value):
        current = self.root
        while current is not None:
            if current.value > value:
                current = current.left
            elif current.value < value:
                current = current.right
            else:
                return True
        else:
            return False

if __name__ == "__main__":
    tree = BinaryTree()
    tree.add_node(9)
    tree.add_node(8)
    tree.add_node(7)
    tree.add_node(15)
    print(tree.find(70))
    tree.find_recursive(7)