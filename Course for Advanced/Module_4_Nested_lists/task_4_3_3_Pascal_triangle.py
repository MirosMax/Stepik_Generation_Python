def pascal(n):
    pascal_matrix = [[1], [1, 1]]  # первые две строки треугольника
    if n > 1:
        # формируем треугольник только из единиц
        for i in range(2, n + 1):
            pascal_matrix.append([1] * (i + 1))
        # заменяем внутренние единицы на суммы двух расположенных над ним чисел
        for i in range(2, n + 1):
            for j in range(1, len(pascal_matrix[i]) - 1):
                pascal_matrix[i][j] = pascal_matrix[i - 1][j - 1] + pascal_matrix[i - 1][j]
    # возвращаем весь треугольник
    return pascal_matrix


n = int(input())
# выводим нужную строку
print(pascal(n)[n])
