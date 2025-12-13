import re

# Level 1

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'[A-Za-z]+', paragraph)
unique_words = set(words)
# words_with_occurrences = {word: words.count(word) for word in unique_words}
words_with_occurrences = sorted([(words.count(word),word) for word in unique_words], key=lambda x: x[0], reverse=True)
print(words_with_occurrences)

point_strs = ['-12', '-4', '-3', '-1', '0', '4', '8']
points = list(map(int, point_strs))
sorted_points = sorted(points)
print(sorted_points)
distance = max(sorted_points) - min(sorted_points)
print(distance)

def is_valid_variable(name):
    return re.match(r'^[A-Za-z]+_?[A-Za-z]+$', name) is not None

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

# Level 3

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    return re.sub(r'[&@%#;$.!?]', '', text)

def most_frequent_words(text):
    words_from_text = re.findall(r'[A-Za-z]+', text)
    unique_words_from_text = set(words_from_text)
    return sorted([(words_from_text.count(word), word) for word in unique_words_from_text], key=lambda x: x[0], reverse=True)[0:3]

cleaned_text = clean_text(sentence)
print(cleaned_text) # I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]