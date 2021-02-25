file = open('secret.txt', 'rt')

text = file.read(5)
print(text)
print(file.read())
print(file.read())

file.close()
