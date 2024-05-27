def sum_abc(abc, a):
    if isinstance(abc, int):
        return abc
    if isinstance(abc, str):
        return len(abc)
    else:
        print("Error", a)
        print(type(abc))
        return 0


def calculate_structure_sum(struct):
    if isinstance(struct, int) or isinstance(struct, str):
        return sum_abc(struct, 1)
    sum_ = 0
    for i in struct:
        if isinstance(i, list):
            sum_ += calculate_structure_sum(i)
        elif isinstance(i, tuple):
            sum_ += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for j in i.keys():
                sum_ += len(j)
            for j in i.values():
                sum_ += calculate_structure_sum(j)
        elif isinstance(i, set):
            sum_ += calculate_structure_sum(i)
        else:
            sum_ += sum_abc(i, 2)
    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
