#1

paris = {
    "name": "Paris",
    "land": "France",
    "capital": True,
    "inhabitants": 2.161,
    "area": 105,
    "airport": ('CDG', 'ORY', 'BVA')
}

marseille = {
    "name": "Marseille",
    "land": "France",
    "capital": False,
    "inhabitants": 0.862,
    "area": 241,
    "airport": ('MRS',)
}


# #2
# print(paris.keys(), marseille.keys())
# print(paris.values(), marseille.values())
# print(paris.items(), marseille.items())


# #3
# print(paris["name"], marseille["name"])
# print(paris["inhabitants"], paris["area"], paris["airport"])


# #4
# density_paris = round(paris["inhabitants"] / paris["area"], 3)
# density_marseille = round(marseille["inhabitants"] / marseille["area"], 3)

# print(f"La ville de {paris['name']} a une densité de {density_paris} habitants par km². Elle comporte {len(paris['airport'])} aéroport(s).")

# print(f"La ville de {marseille['name']} a une densité de {density_marseille} habitants par km². Elle comporte {len(marseille['airport'])} aéroport(s).")


# #5
# paris["inhabitants"] = 2.163
# marseille["inhabitants"] = 0.875

# print(f"La ville de {paris['name']} a une population de {paris['inhabitants']} habitants")
# print(f"La ville de {marseille['name']} a une population de {marseille['inhabitants']} habitants")


# #6
# paris["region"] = 'Île-de-France'
# marseille["region"] = 'Provence-Alpes-Côte d’Azure'

# print(f"La ville de {paris['name']} se trouve dans la région {paris['region']}.")
# print(f"La ville de {marseille['name']} se trouve dans la région {marseille['region']}.")


# #7
# del paris['airport']
# del paris['capital']
# del paris['area']

# print(paris)


# #8
# print(len(paris))


# #9
# def get_density(city):
#     if isinstance(city, dict):
#         density = round(city["inhabitants"] / city["area"], 3)
#         return f"{density} hab/km²"
#     else:
#         return f"{city} is not a dictionnary!"

# print(get_density(paris), get_density(marseille))


# #10
# def get_airport_count(city):
#     return len(city["airport"])

# print(get_airport_count(paris), get_airport_count(marseille))


# #11
# for key in paris:
#     print(key, ':', paris[key])


# #12
# for key in marseille.keys():
#     print(key, ':', marseille[key])

# #13
# for value in paris.values():
#     print(value)

# #14
# for key, value in paris.items():
#     print(key, ':', value)

seoul = {
    'name':'Séoul',
    'land':'Corée du Sud',
    'capital':True, 
    'inhabitants':9.962, 
    'area':606
}

# #15
# def get_most_populated(city_1, city_2):
#     most = max(city_1["inhabitants"], city_2["inhabitants"])

#     if most == city_1["inhabitants"]:
#         return city_1["name"]
#     else:
#         return city_2["name"]


# print(get_most_populated(paris, marseille))

# #16
# def is_in_land(country: str, city_1: dict, city_2: dict) -> list:
#     result = []
#     if city_1['land'] == country:
#         if city_1['capital']:
#             result.append(f"{city_1['name']} (Capital)")
#         else:
#             result.append(city_1['name'])
    
#     if city_2['land'] == country:
#         if city_2["capital"]:
#             result.append(f"{city_2['name']} (Capital)")
#         else:
#             result.append(city_2['name'])

#     return result

# print(is_in_land('France', paris, marseille))

# #17
# def switch_capital_state(city):
#     return not city["capital"]

# print(switch_capital_state(paris))

# #18
# def display_data(city):
#     print(f"La ville {city['name']} comporte {len(city)} données")
#     for key, value in city.items():
#         print(f"{key}: {value}")


# display_data(paris)