from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="wazeyes")

endereco = input("Digite um endereco com número e cidade:")

resultado = str(geolocator.geocode(endereco)).split(',')

if resultado[0] is not None:
    print(f"Endereco completo.:{resultado}\n"
          f"Bairro............:{resultado[0]}\n"
          f"Cidade............:{resultado[1]}\n"
          f"Região............:{resultado[2]}")
