def fun(a, b, c, d, *args, **kwargs):
    print(args)
    print(kwargs)
    return a + b


data = (2, 7, 9, 4)
deta = {'a': 5, 'b': 83, 'c': 2}
print(*data, sep=', ', end='\n\n')
print(*deta)
