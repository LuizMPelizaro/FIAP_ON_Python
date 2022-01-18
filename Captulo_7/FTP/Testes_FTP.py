from ftplib import FTP

ftp_ativo: bool = False
ftp = FTP('ftp.ibge.gov.br')
print(ftp.getwelcome())

usuario: str = input("Digite seu usuario: ")
senha: str = input("Digite sua senha: ")
ftp.login(usuario, senha)

print(f"Diretorio atual de trabalho: {ftp.pwd()}")
ftp.cwd('Pib_Municipios')

print(f"Diretorio atual de trabalho: {ftp.pwd()}")
print(ftp.retrlines('LIST'))
ftp.quit()