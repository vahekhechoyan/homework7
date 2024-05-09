def memorize(func):
    cache = {}
    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return inner

def expensive_function(x):
    print(f"Calculating... for {x}")
    return x ** 2

memorized_expensive_function = memorize(expensive_function)

print(memorized_expensive_function(3))
print(memorized_expensive_function(3))
print(memorized_expensive_function(4))
print(memorized_expensive_function(4))