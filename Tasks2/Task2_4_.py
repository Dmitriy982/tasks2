n = input("Введите строку из нескольких символов через пробел: ").split()
for ind, el in enumerate(n, 1):
    print(ind, el[0:10])
