def add_new_country(country_parameter, visits_parameter, cities_parameter):
    new_dictionary = {}
    new_dictionary["country"] = country_parameter
    new_dictionary["visits"] = visits_parameter
    new_dictionary["cities"] = cities_parameter
    travel_log.append(new_dictionary)

country = input("Insert the country: ") 
visits = int(input("Insert the number of visits: ")) 
list_of_cities = eval(input("Insert the list of cities you visited in this country: ")) 

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")