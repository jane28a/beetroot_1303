def increment(value):
    return value + 1

def list_map(func, sequence):
    print(func)
    return [func(element) for element in sequence]

if __name__ == "__main__":
    print(list_map(len, "I like coffee".split()))
    print(list_map(increment, [25, 79, 104]))