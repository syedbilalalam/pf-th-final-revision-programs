# Question 2
"""Make a dictionary called cities.
Use the names of three cities as keys in your dictionary.
Create a dictionary of information about each city and
include the country that the city is in,
its approximate population, and one fact about that city.
The keys for each city's dictionary should be something
like country, population, and fact. Print the name of each
city and all of the information you have stored about it."""

# Source code
cities = {
    "Karachi": {"country": "Pakistan", "population": "22 million", "fact": "City of Lights"},
    "Istanbul": {"country": "Turkey", "population": "16 million", "fact": "In two continents"},
    "Tokyo": {"country": "Japan", "population": "37 million", "fact": "World's largest metro area"}
}

for city, info in cities.items():
    print(f"City: {city}")

    for info_key, info_val in info.items():
        print(f"{info_key} => {info_val}")