import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


# Define filter_items()
def filter_items(condition, dict_list):

    return [
        item for item in dict_list
        if condition(item)
    ]


# Define aggregate()
def aggregate(aggregation_key, aggregation_function, dict_list):
    values = [
        item[aggregation_key]
        for item in dict_list
    ]

    return aggregation_function(values)


# Print first 5 cities only
print("First 5 cities:")

for city in cities[:5]:
    print(city)
print()


# Print the average temperature of all the cities
print("The average temperature of all the cities:")

avg_temp = aggregate("temperature",
    lambda values: sum(float(value) for value in values)/len(values), cities)

print(avg_temp)
print()


# Print all cities in Germany
print("All the cities in Germany:")

germany_cities = filter_items(lambda city: city["country"] == "Germany", cities)

for city in germany_cities:
    print(city)
print()


# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")

spain_cities = filter_items(lambda city: city["country"] == "Spain"
    and float(city["temperature"]) > 12, cities)

for city in spain_cities:
    print(city)
print()


# Count the number of unique countries
print("The number of unique countries:")

countries = set(city["country"] for city in cities)

print(len(countries))
print()


# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany")

germany_avgtemp = aggregate("temperature",
    lambda values: sum(float(value) for value in values)/len(values), germany_cities)

print(germany_avgtemp)
print()


# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy")

italy_cities = filter_items(lambda city: city["country"] == "Italy", cities)

italy_maxtemp = aggregate("temperature",
    lambda values: max(float(value) for value in values), italy_cities)

print(italy_maxtemp)
print()
