"""
EX4: Дан текстовый файл. Найти длину самой длинной строки.
"""

file = open('Text.txt')
linelist = file.readlines()
file.close()

max_length = len(linelist[0])
for line in linelist:
    if len(line) > max_length:
        max_length = len(line)

print(max_length)
