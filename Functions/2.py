def kley(*strings, sep='='):
    text = ''
    for string in strings:
        text += string + sep
    return text[:-len(sep)]


def test_f(**kwargs):
    for key in kwargs:
        print(key)


test_f(a='Lol', n=10, b=True)
