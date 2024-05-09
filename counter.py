def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

print(counter())  
print(counter())  
print(counter())