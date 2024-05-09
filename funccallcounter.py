def function_call_counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        return count, result
    return inner

def example_function(x):
    return x * 2

counter_example_function = function_call_counter(example_function)

print(counter_example_function(3))  
print(counter_example_function(4))  
print(counter_example_function(5)) 