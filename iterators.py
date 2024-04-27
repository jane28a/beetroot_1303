from collections.abc import Iterable

class SequenceIterator:

    def __init__(self, sequence):
        if isinstance(sequence, Iterable):
            self.sequence = sequence
        else:
            self.sequence = list()

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.sequence):
            element = self.sequence[self._index]
            self._index += 1
            return element
        else:
            raise StopIteration()

class EvenNumberIterator:

    def __init__(self, limit=100):
        self.value = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.value < self.limit:
            self.value += 2
            return self.value
        else:
            raise StopIteration()


if __name__ == "__main__":
    for element in SequenceIterator([1, 2, 3]).sequence:
        print(element)

    for element in EvenNumberIterator():
        print(element)