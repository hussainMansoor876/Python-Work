sentence = str(input("Enter text:"))
characters = {}

for character in sentence:
    characters[character] = characters.get(character, 0) + 1
print(characters)
for key,value in characters.items():
    print(key,",",value)