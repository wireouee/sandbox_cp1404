word_collection = {}
text = input("Text: ")
word = text.split(' ')
print(word)
for a in word:
    word_collection[a] = word_collection.get(a, 0)+1
word_collection = sorted(word_collection.items())
for key, value in word_collection:
    print("{} : {}".format(key, value))
