word_to_frequency = {}

text = input("Text: ")
words = text.split(" ")
for word in words:
    frequency = word_to_frequency.get(word, 0)
    word_to_frequency[word] = frequency + 1

longest_word = max(len(word) for word in words)
for word in words:
    print(f"{word:{longest_word}} : {word_to_frequency[word]}")
