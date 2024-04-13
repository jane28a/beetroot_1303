def pop_b(data):
    data.pop("b")
    return data

def get_data(callback_func):
    # imagine it retrieves data from web
    data = {"a": 1, "b": 2}
    return callback_func(data)

if __name__ == "__main__":
    get_data(print)
    data = get_data(pop_b)
    print(data)