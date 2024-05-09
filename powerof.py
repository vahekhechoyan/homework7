def power_of(exp):
    def inner(x):
        return x ** exp
    return inner

square = power_of(2)
print(square(3)) 

cube = power_of(3)
print(cube(3))  