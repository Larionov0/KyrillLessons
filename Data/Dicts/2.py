def letters_counter(string):
    """
    Считает количество каждой буквы в строке.
    :param string: str
    'I love pizza and I love Python'
    :return: dict[letters: counts]
    """
    letters_counts = {}
    for letter in string:
        if letter in letters_counts:
            letters_counts[letter] += 1
        else:
            letters_counts[letter] = 1
    return letters_counts


dct = letters_counter("""Вначале чуть слышный хруст, затем сахарный взрыв, осколки которого оседают в уголках губ, в то время как сладкий вкус начинки уже растекается во рту…
Миндальное печенье «макарун», частица небесного наслаждения, умещающаяся между указательным и большим пальцем, – самое современное из классических произведений французских кондитеров.""")
for letter in dct:
    print(letter + ":", dct[letter])
