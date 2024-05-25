class Node:

    def __init__(self, _id, value, next_node=None):
        self.id = _id
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"Node {self.id}: value {self.value}"

class LinkedList:

    def __init__(self):
        self.head = None

    def __len__(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        pass

    def add_node(self, value):
        _id = len(self) + 1
        if not self.head:
            self.head = Node(_id, value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(_id, value)

    def print_nodes(self):
        current = self.head
        while current:
            print(current)
            current = current.next

class OrderedLinkedList(LinkedList):

    def add_node(self, value):
        _id = len(self) + 1
        if not self.head or self.head.value > value:
            self.head = Node(_id, value, self.head)
        else:
            current = self.head
            while current.next:
                if current.next.value > value:
                    break
                current = current.next
            current.next = Node(_id, value, current.next)

if __name__ == "__main__":
    """
    container = LinkedList()
    container.add_node(10)
    container.add_node(20)
    container.add_node(30)
    print(len(container))
    container.print_nodes()
    """

    ordered_container = OrderedLinkedList()
    ordered_container.add_node(40)
    ordered_container.add_node(20)
    ordered_container.add_node(60)
    ordered_container.add_node(50)
    ordered_container.add_node(30)
    ordered_container.print_nodes() #20, 30, 40, 50, 60

    """
    for node in container:
        print(node)
    """