favourite_languages = {'Talha': ['python', 'C++'], 'Ahmed': ['C++', "Java"], 'Arslan': ['Kotlin', 'java'], 'Usman': ['C', 'Flutter']}
# Show all responses for each person.
for name, languages in favourite_languages.items():
    print(name + ": ")
    for lang in languages:
        print("* " + lang)