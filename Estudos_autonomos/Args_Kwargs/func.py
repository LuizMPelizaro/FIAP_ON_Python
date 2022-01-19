def world_cup_titles(country, *args) -> None:
    """Imprime o pais e os anos o qual elke foi campeão de copa do mundo"""
    print(f'Country: {country}')

    for title in args:
        print(f'year: {title}')


def calculate_price(value: float, **kwargs) -> float:
    """Calcula o preço de um determinado item , fazendo as operações de disconto e de taxação"""
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')

    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount

    return value
