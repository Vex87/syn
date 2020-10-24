from PyDictionary import PyDictionary
dictionary = PyDictionary()

while True:
    type = input("Enter the function prefix: ")
    if type == "m":
        print(dictionary.meaning(input("Enter a word to retrieve the meaning: ")))
    elif type == "s":
        print(dictionary.synonym(input("Enter a word to retrieve synonyms: ")))
    elif type == "a":
        print(dictionary.antonym(input("Enter a word to retrieve antonyms: ")))