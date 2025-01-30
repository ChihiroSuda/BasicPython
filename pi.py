text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

words = text.lower().replace(".", " ").replace(","," ").split()
word_lengths = list(map(len, words))

for word, length in zip(words, word_lengths):
    print(f"{word}:{length}文字")