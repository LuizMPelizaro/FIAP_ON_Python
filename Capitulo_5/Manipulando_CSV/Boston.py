from Funcoes import *

print(f'O total de voos foi de {total_voos_2014("economic-indicators.csv")}')

ano: int = int(input("Digite o ano do qual deseja saber os dados: "))

print(f'{mes_ano_ocorreu_maior_transito_aerio("economic-indicators.csv")}\n'
      f'{numero_passageiros("economic-indicators.csv", ano)}\n'
      f'{maior_media_valor_hotel("economic-indicators.csv", ano)}')
