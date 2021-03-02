"""
EX5: Дан текстовый файл. Посчитать сколько раз в нем встречается заданное пользователем слово.
"""

file = open('Text.txt', encoding='utf-8')
text = file.read()
file.close()

textN = text.lower().split()
keyW = input('Введите слово: ').lower()
countW = 0

for word in textN:
    clean_word = word.strip('-=.,!?:{}"\/|')
    if keyW == clean_word:
        countW +=1
print(countW)