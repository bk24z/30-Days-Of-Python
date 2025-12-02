# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent)) # Add parent directory to Python path
from data.countries import countries

# Level 2 Exercises

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25]
ages.sort()
print(ages)
min = ages[0]
max = ages[-1]
print(min)
print(max)
ages += [min, max]
print(ages)
ages.sort()
print(ages)
if len(ages) % 2 != 0:
    print(ages[int(len(ages)/2)])
else:
    print(
        (
            ages[int(math.floor(len(ages)/2)-1)] + ages[int(math.ceil(len(ages)/2)-1)]
        )/2
    )
average = sum(ages)/len(ages)
print(average)
print(max-min)
print(abs(min-average))
print(abs(max-average))

# countries = countries[1:]

if len(countries) % 2 != 0:
    print(countries[int(len(countries)/2)])
else:
    print(countries[int(math.floor(len(countries)/2) - 1)],countries[int(math.ceil(len(countries)/2) - 1)])

ch, ru, us, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(ch)
print(ru)
print(us)
print(scandic)