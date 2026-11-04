def to_dict(items):
    return {i: value for i, value in enumerate(items)}


print(to_dict(["a", "b", "c"]))
print(to_dict([10, 20, 30]))
print(to_dict([]))
