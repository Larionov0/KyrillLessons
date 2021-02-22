def decor(func):
    def new_func(*args, **kwargs):  # args = (1, 4)  kwargs={'a': 2, 'b': 5}
        print('-' * 40)
        func(*args, **kwargs)  # === func(a=2, b=5)
        print('-' * 40)
    return new_func


@decor
def helloer(name):
    print(f"Hello, {name}!")


@decor
def sum_ab(a, b):
    print(a + b)


@decor
def print_names(*names):
    for name in names:
        print(name)


helloer('Bob')
sum_ab(b=1, a=4)
print_names('a', 'b', 'c')
