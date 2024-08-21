def pascal(n):
    # начальная строка
    cur_seq = [1]
    for _ in range(n):
        # добавляем нули по бокам к текущей строке строке
        cur_seq = [0] + cur_seq + [0]
        # тут будет храниться новая строка
        new_seq = []
        for i in range(len(cur_seq) - 1):
            # добавляем в новую строку сумму соседних элементов текущей строки
            new_seq.append(cur_seq[i] + cur_seq[i + 1])
        # теперь новая строка становится нашей текущей строкой
        cur_seq = new_seq
    return cur_seq
n = int(input())

print(pascal(n))