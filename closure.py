def my_map(func, *iterables, handle_exceptions=None):
    if handle_exceptions is None:
        handle_exceptions = lambda e: None

    min_length = min(len(iterable) for iterable in iterables)
    for i in range(min_length):
        try:
            args = []
            for it in iterables:
                args.append(it[i])
            yield func(*args)
        except Exception as e:
            yield handle_exceptions(e)

def my_zip(*iterables, fillvalue=None):
    min_length = min(len(iterable) for iterable in iterables)
    for i in range(min_length):
        tuple_values = []
        for iterable in iterables:
            if i < len(iterable):
                tuple_values.append(iterable[i])
            else:
                tuple_values.append(fillvalue)
        yield tuple(tuple_values)

def my_reduce(func, iterable, initial=None):
    accum_value = initial if initial is not None else iterable[0] if len(iterable) > 0 else None
    for item in iterable[1:]:
        accum_value = func(accum_value, item)
    return accum_value

def my_filter(func, iterable):
    index = 0
    for item in iterable:
        if func(item):
            yield index, item
        index += 1

def my_enumerate(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1

def log_function_calls(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' called with args: {args}, kwargs: {kwargs}. Returned: {result}")
        return result
    return wrapper

def pipeline(inputs, funcs):
    result = inputs
    for func in funcs:
        result = [func(x) for x in result]
    return result

@log_function_calls
def add_one(x):
    return x + 1

@log_function_calls
def multiply_by_two(x):
    return x * 2

@log_function_calls
def power_of_three(x):
    return x ** 3

inputs = [1, 2, 3, 4, 5]
functions = [add_one, multiply_by_two, power_of_three]

result = pipeline(inputs, functions)
print(result)