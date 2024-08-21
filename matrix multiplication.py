#1 матрица
x = input().split()
n1, m1 = int(x[0]), int(x[1])
matrix1 = [[int(x) for x in input().split()]for _ in range(n1)] 
c = input()

#2 матрица
x = input().split()
m2, k2 = int(x[0]), int(x[1])
matrix2 = [[int(x) for x in input().split()]for _ in range(m2)]

# 3 матрица, пока что пустая
matrix3 = [[0] * k2 for _ in range(n1)]

for i in range(n1):
    for j in range(k2):
        for k in range(m1):
            matrix3[i][j] += matrix1[i][k] * matrix2[k][j]

for i in matrix3:
    print(*i)