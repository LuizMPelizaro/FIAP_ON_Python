import os
from ftplib import FTP


def escreverLinha(data) -> None:
    arq.write(data)
    arq.write(os.linesep)


ftp_ativo = False
ftp = FTP('ftp.ibiblio.org')

print(ftp.getwelcome())
ftp.login()

arquivo = "LEIAME"
ftp.set_pasv(ftp_ativo)
# Definimos abrir/criar arquivo chamado LEIAME
with open(arquivo, 'w') as arq:
    # Utilizamos o metodo retrlines(), que é formado pelos parametros :
    # O primeiro o que especifica o retorno (RETR) e o nome do arquivo que será retornado('RETR README')
    # O segundo é a função que foi criada acima que recebera o conteudo da linha arq.write(data)
    ftp.retrlines('RETR README', escreverLinha)
ftp.quit()
