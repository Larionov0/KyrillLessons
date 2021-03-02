"""
Дан текстовый файл. Удалить из него последнюю строку.
Результат записать в другой файл.
"""

file = open('Text.txt', encoding='utf-8')
lines = file.readlines()
file.close()
lines1 = lines[:-1]

fileN = open("NewText.txt", "wt", encoding='utf-8')
fileN.writelines(lines1)
fileN.close()
