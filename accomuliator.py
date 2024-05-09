def accumulator(initial):
    total = initial
    def inner(number):
        nonlocal total
        total += number
        return total
    return inner

my_accumulator = accumulator(0)

print(my_accumulator(5))  
print(my_accumulator(3))  
print(my_accumulator(10))  