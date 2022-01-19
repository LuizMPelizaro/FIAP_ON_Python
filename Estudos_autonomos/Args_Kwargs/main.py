from func import world_cup_titles, calculate_price

world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')
world_cup_titles('Espanha', '2010')

final_price = calculate_price(100.0, discount=5, tax_percentage=10)
print(f'O valor final é de {final_price}')
