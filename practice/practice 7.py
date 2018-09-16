sentence = "The quick brown fox jumped over the lazy dog."
characters = {}

for character in sentence:
    characters[character] = characters.get(character, 0) + 1

print(characters)