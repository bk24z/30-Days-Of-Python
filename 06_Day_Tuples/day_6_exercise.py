# Level 1
empty = ()
brothers = ("Bro1","Bro2")
sisters = ("Sis1","Sis2")
siblings = brothers + sisters
print(siblings)
print(len(siblings))
family_members = siblings + ("Mum","Dad")
print(family_members)

# Level 2

siblings = family_members[0:4]
parents = family_members[4:6]
print(siblings,parents)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('lettuce','cabbage','carrot','spinach')
animals = ('dog','cat','mouse','snake')
food_stuff_tp = fruits + vegetables + animals
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

import math

if len(food_stuff_lt) % 2 != 0:
    print(food_stuff_lt[int(len(food_stuff_lt)/2)])
else:
    print(food_stuff_lt[int(math.floor(len(food_stuff_lt)/2) - 1)],food_stuff_lt[int(math.ceil(len(food_stuff_lt)/2))])

print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)