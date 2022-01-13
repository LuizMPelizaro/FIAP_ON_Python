from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="wazeyes")

latitude: float = float(input("Digite a latitude..:"))
logitude: float = float(input("Digite a longitude.:"))

resultado = str(geolocator.reverse(f'{latitude}, {logitude}')).split(',')
if resultado is not None:
    print(f"Endereco completo.:{resultado}\n"
          f"Dado 1............:{resultado[0]}\n"
          f"Dado 2............:{resultado[1]}\n"
          f"Dado 3............:{resultado[2]}")
