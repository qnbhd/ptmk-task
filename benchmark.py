def bench(func):
    """
    decorator-function for function benchmark
    :param func: function to test
    :return: -
    """
    import time

    def wrapper(*args, **kwargs):
        start = time.monotonic()  # monotonic - correct for benchmark
        return_value = func(*args, **kwargs)
        end = time.monotonic()
        print('[*] Time: {} seconds.'.format(end - start))
        return return_value

    return wrapper
