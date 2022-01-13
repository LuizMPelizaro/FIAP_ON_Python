from Capitulo_6.Geopy.Exercicio.funcoes import gravar_arquivo, ler_arquivo, formatar_endereco, capturar_cordenadas

# geolocator = Nominatim(user_agent="wazeyes")
dicionario = ler_arquivo("entrada.json")
# lista = dicionario["endereco"]
# endereco = lista[0] + "," + lista[1] + " - " + lista[2]
# print(endereco)
# location = geolocator.geocode(endereco)
# # saida = {"coordenadas": (location.latitude, location.longitude)}
# print(type(saida))
gravar_arquivo("saida.json", capturar_cordenadas(formatar_endereco(dicionario)))
