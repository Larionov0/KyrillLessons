def line(n=30):
    print('-' * n)


def is_float(number_str):
    if '.' in number_str:
        if number_str.count('.') != 1 or not all([num_str.isdigit() for num_str in number_str.split('.')]):
            return False
    else:
        if not number_str.isdigit():
            return False
    return True


def input_float(question, error_msg='Use digits only :)'):
    while True:
        number_str = input(question)
        if not is_float(number_str):
            print(error_msg)
            continue
        return float(number_str)


def input_int(question, min_=None, max_=None, error_msg='Use digits only :)'):
    while True:
        number_str = input(question)
        if not number_str.isdigit():
            print(error_msg)
            continue
        number = int(number_str)
        if min_ and number < min_:
            print('Too small')
            continue
        if max_ and number > max_:
            print('Too big')
            continue
        return number


def input_str(question, min_len=0, max_len=100, error_msg='Wrong length'):
    while True:
        ans = input(question)
        if not ans.isalpha():
            print('Use only alpha symbols')
        elif len(ans) < min_len or len(ans) > max_len:
            print(error_msg)
        else:
            return ans

