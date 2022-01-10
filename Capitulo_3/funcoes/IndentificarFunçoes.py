def preencher_inventario(inventario: list) -> None:
    resposta: str = "S"
    while resposta == "S":
        equipamento: list = [input("Equipamento: "),
                             int(input("Valor: ")),
                             int(input("Numero Serie: ")),
                             input("Departamento; ")]
        inventario.append(equipamento)
        resposta: str = input("Digite S para inserir um novo item").upper()


def exibir_inventario(lista: list) -> None:
    for elemento in lista:
        print(f'Nome......: {elemento[0]}\n'
              f'Valor.....: {elemento[1]}\n'
              f'Numero Serie: {elemento[2]}\n'
              f'Departamento: {elemento[3]}\n')


def buscar_no_inventario(lista: list) -> None:
    item: str = input("Digite o equipamento que deseja: ")
    for elemento in lista:
        if item == elemento[0]:
            print(f'Valor.....: {elemento[1]}\n'
                  f'Numero Serie: {elemento[2]}\n')


def depreciacao(lista: list) -> None:
    item: str = input("Digite o equipamento que deseja: ")
    for elemento in lista:
        if item == elemento[0]:
            print(f'Valor antigo: {elemento[1]}')
            elemento[1] = elemento[1] * 0.9
            print(f'Valor novo: {elemento[1]}')


def excluir(lista: list) -> str:
    numero_serie: int = int(input("digite o numero de serie do item que deseja excluir"))
    for elemento in lista:
        if numero_serie == elemento[2]:
            lista.remove(elemento)
        return "Item excluido"
