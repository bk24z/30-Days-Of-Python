numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([i for i in numbers if i <= 0])

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print([item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2])

print([tuple([x] + [x ** i for i in range(6)]) for x in range(11)])

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries])

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print([' '.join(name[0]) for name in names])

print((lambda m,x,y: y-m*x)(2,2,0))