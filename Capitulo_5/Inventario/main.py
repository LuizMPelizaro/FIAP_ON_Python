from Capitulo_5.Inventario.funcoes import opicoes, persitir_em_arquivo, exibir_ativos_processados, registro_ativo

invetario: dict = {}
opicao: int = opicoes()

while 4 > opicao > 0:
    if opicao == 1:
        registro_ativo(invetario)
    elif opicao == 2:
        persitir_em_arquivo(invetario)
    elif opicao == 3:
        exibir_ativos_processados("inventario.csv")
    opicao = opicoes()

# Usando o metodo find
# # A varivel linha descarta o numero patrimonial
# separacao = linha[linha.find(";") + 1:-1]
# # A separacao ja pega o dado filtrado sem o numero patrimonial
# data = separacao[0:separacao.find(";")]
# # Neste update da varivel separacao ela descarta a data
# separacao = separacao[separacao.find(";") + 1:-1]
# # Pega a descrição
# descricao = separacao[0:separacao.find(";")]
# # Pega o departamento
# # O metodo rfind começa a leitura da direita para a esquerda
# departamaento = linha[linha.rfind(";") + 1:-1]
# print(f"Data........:{data}\n"
#       f"Descrição...:{descricao}\n"
#       f"Departamento:{departamaento}\n")
