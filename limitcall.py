def limit_call_function(func, max_calls):
    calls = 0
    def inner(*args, **kwargs):
        nonlocal calls
        if calls < max_calls:
            calls += 1
            return func(*args, **kwargs)
        else:
            return "Limit reached for this function"
    return inner

def my_function():
    return "Function called"

limited_function = limit_call_function(my_function, 3)

for _ in range(5):
    result = limited_function()
    print(result)