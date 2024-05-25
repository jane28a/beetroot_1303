class OrderedList:

    def __init__(self):
        self.elements = list()

    def insert(self, value):
        ...


if __name__ == "__main__":
    container = OrderedList()
    container.insert(40)
    container.insert(20)
    container.insert(60)
    container.insert(50)
    container.insert(30)
    print(container.elements) #[20, 30, 40, 50, 60]
