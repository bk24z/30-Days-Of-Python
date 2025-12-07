# Level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Company1','Company2'])
print(it_companies)
# remove() will raise an error if the item is not found
# but discard() doesn't raise any errors

# Level 2

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.update(B))
print(B.update(A))
print(A.symmetric_difference(B))
del A
del B

# Level 3

ages_set = set(age)
print(len(age))
print(len(ages_set))

'''
String -> group of characters
List -> group of items
Tuple -> immutable group of items
Set -> unordered, unindexed group of unique items
'''

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
print(words)
unique_words = set(words)
print(unique_words)