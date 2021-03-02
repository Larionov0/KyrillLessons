"""
Дан текстовый файл. Необходимо создать новый файл и записать в него следующую статистику по исходному файлу:
■ Количество символов - DONE
■ Количество строк - DONE
■ Количество гласных букв - DONE
■ Количество согласных букв - DONE
■ Количество циф

"""
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

file = open('Text.txt')
text = file.read()
file.close()

file = open('Text.txt')
lines = file.readlines()
file.close()

# Количество символов:
countS = 0
for symbol in text:
        countS += 1

# Количество строк:
countL = len(lines)

# Количество гласных букв:
countV = 0
for symbol in text:
    if symbol in vowels:
        countV += 1

# Количество согласных букв:
countC = 0
for symbol in text:
    if symbol in consonants:
        countC += 1

# Количество цыфр:
countD = 0
for digit in text:
    if digit.isdigit():
        countD += 1

file = open('Stat.txt', 'wt')
file.write(f'Q-ty of symbols in file = {countS}\n')
file.write(f'Q-ty of lines in file = {countL}\n')
file.write(f'Q-ty of vowels in file = {countV}\n')
file.write(f'Q-ty of consonants in file = {countC}\n')
file.write(f'Q-ty of digits in file = {countD}\n')
file.close()

