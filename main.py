import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print("Only letters in alphabet are allowed.")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
