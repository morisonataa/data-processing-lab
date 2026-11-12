import csv, os

class Table:
    def __init__(self, data):
        self.data = data

    def filter_items(self, condition):
        filtered_data = [ item for item in self.data if condition(item)]

        return Table(filtered_data)

    def aggregate(self, aggregation_key, aggregation_function):
        values = [ item[aggregation_key] for item in self.data ]

        return aggregation_function(values)


class DataLoader:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        with open(self.filename, encoding="utf-8", newline="") as f:
            rows = csv.DictReader(f)
            data = [dict(row) for row in rows]

        return Table(data)


location = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(location, "Cities.csv")

loader = DataLoader(filename)
cities = loader.load()


# Print first 5 cities only
print("First 5 cities:")

for city in cities.data[:5]:
    print(city)
print()


# Print the average temperature of all the cities
print("The average temperature of all the cities:")

avg_temp = cities.aggregate("temperature",
    lambda values: sum(float(value) for value in values)/len(values))

print(avg_temp)
print()


# Print all cities in Germany
print("All the cities in Germany:")

germany_cities = cities.filter_items(lambda city: city["country"] == "Germany")

for city in germany_cities.data:
    print(city)
print()


# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")

spain_cities = cities.filter_items(lambda city: city["country"] == "Spain"
    and float(city["temperature"]) > 12)

for city in spain_cities.data:
    print(city)
print()


# Count the number of unique countries
print("The number of unique countries:")

countries = set(city["country"] for city in cities.data)

print(len(countries))
print()


# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany")

germany_avgtemp = germany_cities.aggregate("temperature",
    lambda values: sum(float(value) for value in values)/len(values))

print(germany_avgtemp)
print()


# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy")

italy_cities = cities.filter_items(lambda city: city["country"] == "Italy")

italy_maxtemp = italy_cities.aggregate("temperature",
    lambda values: max(float(value) for value in values))

print(italy_maxtemp)
print()