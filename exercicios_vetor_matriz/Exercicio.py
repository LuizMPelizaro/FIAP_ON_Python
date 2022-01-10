A: list[int] = [1, 0, 5, -2, -5, 7]
soma = 0
for numero in range(0, len(A)):
    if numero == 0 or numero == 1 or numero == 5:
        soma = A[numero] + soma
    elif numero == 4:
        A[numero] = 100
print(f'Valor da soma {soma}')

for numero in range(0, len(A)):
    print(f'{numero}-{A[numero]}')
