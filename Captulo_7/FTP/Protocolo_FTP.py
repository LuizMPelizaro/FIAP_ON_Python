from ftplib import FTP

ftplib: bool = False
# Criasse um objeto para representar uma conexão FTP ,
# para isso se usa o metodo FTP() , que precisa apenas do endereço do servidor FTP , no exemplo foi utilizado
# esse endereço , pode se entrar pela web
ftp = FTP('ftp.ibiblio.org')
print(type(ftp))
print(ftp.getwelcome())
usuario = input("Digite o seu usuario: ")
senha = input("Digite a senha: ")
ftp.login(usuario, senha)

# O codigo pwd() retorna o endereço atual de trabalho, ou seja retona o diretorio que voce se encontra atualmente
print(f"Diretorio atual de trabalho: {ftp.pwd()}")
ftp.cwd('pub')
print(f"Diretorio corrente: {ftp.pwd()}")

# Mostra todos os arquivos do diretorio
print(ftp.retrlines('LIST'))
ftp.quit()
