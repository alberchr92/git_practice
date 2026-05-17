favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#Schlüssel sortiert durchlaufen
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#Werte durchlaufen
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())