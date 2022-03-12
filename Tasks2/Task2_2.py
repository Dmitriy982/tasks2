List = input("Введите значения списка через пробел: ").split()
n = 0
i = 0
while i + 1 < len(List):
    n = List[i+1]
    List[i+1] = List[i]
    List[i] = n
    i = i+2
print(List)


