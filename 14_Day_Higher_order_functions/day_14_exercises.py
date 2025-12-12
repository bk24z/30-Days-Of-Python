from data.countries import countries as all_countries
from data.countries_data import countries_data
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Level 2

uppercase_countries = list(map(lambda c: c.upper(), countries))
print(uppercase_countries)

square_numbers = list(map(lambda n: n ** 2, numbers))
print(square_numbers)

uppercase_names = list(map(lambda n: n.upper(), names))
print(uppercase_names)

countries_without_land = list(filter(lambda c: 'land' not in c, countries))
print(countries_without_land)

six_char_countries = list(filter(lambda c: len(c) == 6, countries))
print(six_char_countries)

six_or_more_char_countries = list(filter(lambda c: len(c) >= 6, countries))
print(six_char_countries)

start_with_E_countries = list(filter(lambda c: c.startswith('E'), countries))
print(start_with_E_countries)

# Not sure what 8 means

get_string_lists = lambda l: list(filter(lambda i: type(i) == type('str'), l))
print(get_string_lists([1, '2', 3]))

print(reduce(lambda x, y: x + y, numbers))

print(f"{reduce(lambda x, y: x + ", " + y, countries[0:-1])}, and {countries[-1]} are north European countries")


def categorise_countries():
    return list(filter(lambda c: c.endswith('land'), all_countries))


print(categorise_countries())


def countries_and_starting_letters():
    starting_letters = sorted(set(country[0] for country in all_countries))
    return {letter: sum(1 for c in all_countries if c[0] == letter) for letter in starting_letters}


print(countries_and_starting_letters())


def get_first_ten_countries():
    return all_countries[:10]


print(get_first_ten_countries())


def get_last_ten_countries():
    return all_countries[-10:]


print(get_last_ten_countries())

# Level 3

countries_sorted_by_name = sorted(countries_data, key=lambda c: c['name'])
print(countries_sorted_by_name)
countries_sorted_by_capital = sorted(countries_data, key=lambda c: c['capital'])
print(countries_sorted_by_capital)
countries_sorted_by_population = sorted(countries_data, key=lambda c: c['population'])
print(countries_sorted_by_population)
# Not sure what it means by "the ten most spoken languages by location"
ten_most_populated_countries = list(reversed(countries_sorted_by_population[-10:]))
print(ten_most_populated_countries)
