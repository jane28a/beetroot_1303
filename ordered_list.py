class OrderedList:

    def __init__(self):
        self.elements = list()

    def insert(self, value):
        self.elements = (
                [element for element in self.elements if element < value]
                + [value]
                + [element for element in self.elements if element > value]
            )

    def binary_search(self, value):
        low = 0
        high = len(self.elements) - 1

        while low <= high:
            mid = (high + low) // 2
            if self.elements[mid] > value:
                high = mid - 1
            elif self.elements[mid] < value:
                low = mid + 1
            else:
                return mid # self.elements[mid], True

        return -1 # False, "Not found"

    def recursive_binary_search(self, *args, **kwargs):
        pass


if __name__ == "__main__":
    # my_list = ["a", "b"] * 40
    # print(my_list)
    container = OrderedList()
    container.insert(40)
    container.insert(20)
    container.insert(60)
    container.insert(50)
    container.insert(30)
    print(container.elements) #[20, 30, 40, 50, 60]

    print(container.binary_search(35))
