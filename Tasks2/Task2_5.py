my_list = [7, 5, 3, 3, 2]
n = int(input("Введите число рейтинга: "))
my_list.append(n)
a = 1
while a < len(my_list):
    for i in range(len(my_list)-a):
        if my_list[i] < my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    a += 1
print(my_list)