def simple_gen():
    sequence = [1, 2, 3]
    index = 0
    while index < len(sequence):
        yield sequence[index] #
        index += 1

def sequential_yield():
    sequence = [1, 2, 3]
    yield sequence[0] 
    yield sequence[1]
    yield sequence[2]

def simple_ret():
    sequence = [1, 2, 3]
    index = 0
    while index < len(sequence):
        return sequence[index]
        index += 1

if __name__ == "__main__":
    element = (x for x in [1, 2, 3])
    print(element)

    #for val in sequential_yield():
    #    print(val)