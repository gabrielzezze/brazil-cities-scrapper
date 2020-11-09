import unidecode

def generate_file_name(uf, city, termination):
    formatted_uf = uf.lower()
    unaccented_city = unidecode.unidecode(u'{}'.format(city))
    formatted_city = unaccented_city.lower().replace(' ', '-').replace("'", "")

    return f'{formatted_city}_{formatted_uf}.{termination}'
