def expand(numbers):
    return [list(range(n + 1)) for n in numbers]


print(expand([1, 2, 3]))
print(expand([0, 4]))
print(expand([]))
