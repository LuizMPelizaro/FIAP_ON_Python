from funcoes import exibir_ativos, registro_ativo, opicoes, ler_arquivo

arquivo: str = 'inventario_json.json'
inventario: dict = ler_arquivo(arquivo)
opicao: int = opicoes()
while 0 < opicao < 3:
    if opicao == 1:
        registro_ativo(inventario, arquivo)
    elif opicao == 2:
        exibir_ativos(arquivo)
    opicao = opicoes()
