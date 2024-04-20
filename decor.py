from functools import wraps

def catch_error(print_message):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                print("It worked")
                return result
            except KeyError:
                if print_message:
                    print("Error happened")
                else:
                    pass
        return wrapper
    return inner

# raises_error = catch_error(print_message)(raises_error)

@catch_error(print_message=True)
def raises_error(the_dict):
    """
        Example docstring
        Function description here
    """
    return the_dict["something"]

if __name__ == "__main__":
    print(raises_error.__name__)
    print(raises_error.__doc__)