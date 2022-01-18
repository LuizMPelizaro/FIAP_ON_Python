from funcoes import conect_ftp, login_ftp, opicao, listar_arquivo, definir_diretorio, baixa_arquivo

# ftp.ibge.gov.br
ftp_ativo: bool = False
# base_de_dados_2010_2019_txt.zip
ftp = conect_ftp(input("Digite o servidor FTP que deseja conectar: "))
print(login_ftp(ftp, input("Digite o usuario: "), input("Digite a senha:")))

menu: int = 1
while 0 < menu < 4:
    if menu == 1:
        listar_arquivo(ftp)
    elif menu == 2:
        definir_diretorio(ftp, input("Digite o enderço do diretorio"))
    elif menu == 3:
        baixa_arquivo(ftp, input(
            "Digite o tipo do arquivo que deseja baixar\n <B> para binario\n Qualquer outra letra para ASCII: ").upper(),
                      input("Digite o nome do arquivo"))
    menu = opicao()

ftp.close()
