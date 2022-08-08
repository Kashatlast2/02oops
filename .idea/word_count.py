str = 'This is an awesome occasion. This has never happened before.'

# key:value - key value pair

char_occurences = {} # {} - dict, [] - list

for char in str:
    char_occurences[char] = char_occurences.get(char, 0) + 1

word_occurences = {} # {} - dict, [] - list

for word in str.split():
    word_occurences[word] = word_occurences.get(word, 0) + 1

print(char_occurences)
print(word_occurences)