# Дан список A размера N. Найти максимальный элемент из его элементов с нечетными номерами: A1, A3, A5, ... .

a = [12, 14, -2, 18, 43, 15, 29, -35, 48, 52, 55, 61, 1]
n = len(a)
b = []

for i in range(n):
    if i % 2 != 0:
        b.append(a[i])

print('Максимальный нечётный элемент: ', max(b))
print('Программа завершена!')
