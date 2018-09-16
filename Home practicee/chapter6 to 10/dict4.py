favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print(list(favorite_languages.values()))
print(list(favorite_languages))
print(list(favorite_languages.items()))
for language in set(favorite_languages.values()):
    print(language.title())
