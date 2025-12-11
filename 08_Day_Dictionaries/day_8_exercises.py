dog = {}

dog['name'] = 'Dog'
dog['color'] = 'Red'
dog['breed'] = 'Chihuahua'
dog['legs'] = 4
dog['age'] = 30

student = {
    'first_name': 'Student',
    'last_name': 'Student',
    'gender': 'Male',
    'age': 18,
    'marital_status': 'Married',
    'skills': ['Python', 'JavaScript'],
    'country': 'United Kingdom',
    'city': 'London',
    'address': {
        'street': ' Space Street',
        'postcode': 'S1P F49'
    }
}

print(len(student))

print(student['skills'])

print(type(student['skills']))

student['skills'].extend(['Swift', 'Rust'])
print(student['skills'])

print(list(student.keys()))

print(list(student.values()))

print(list(student.items()))

del student['age']

del dog
