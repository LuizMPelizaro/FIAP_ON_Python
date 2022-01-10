inventario: list = []
resposta: str = "S"
while resposta == "S":
    equipamento: list = [input("Equipamento: "),
                         int(input("Valor: ")),
                         int(input("Numero Serie: ")),
                         input("Departamento; ")]
    inventario.append(equipamento)
    resposta: str = input("Digite S para inserir um novo item").upper()

for elemento in inventario:
    print(f'Nome......: {elemento[0]}\n'
          f'Valor.....: {elemento[1]}\n'
          f'Numero Serie: {elemento[2]}\n'
          f'Departamento: {elemento[3]}\n')

busca: str = input("Digite o equipamento que deseja: ")
for elemento in inventario:
    if busca == elemento[0]:
        print(f'Valor.....: {elemento[1]}\n'
              f'Numero Serie: {elemento[2]}\n')

depreciacao: str = input("Digite o nome do item que deseja depreciar")
for elemento in inventario:
    if depreciacao == elemento[0]:
        print(f'Valor antigo: {elemento[1]}')
        elemento[1] = elemento[1] * 0.9
        print(f'Valor novo: {elemento[1]}')

numero_serie: int = int(input("digite o numero de serie do item que deseja excluir"))
for elemento in inventario:
    if numero_serie == elemento[2]:
        inventario.remove(elemento)

for elemento in inventario:
    print(f'Nome......: {elemento[0]}\n'
          f'Valor.....: {elemento[1]}\n'
          f'Numero Serie: {elemento[2]}\n'
          f'Departamento: {elemento[3]}\n')

# funçoes para listas numericas
valores: list[int] = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print(f'O equipamento mais caro custa {max(valores)}\n'
          f'O equipamento mais barato custa {min(valores)}\n'
          f'A soma dos valores dos equipamentos é de {sum(valores)}')
