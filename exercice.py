#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    result = len(string) % 2 == 0
    return result


def remove_third_char(string: str) -> str:
    letters_except_third = string [:2] + string [3:]
    new_string = letters_except_third
    return new_string


def replace_char(string: str, old_char: str, new_char: str) -> str:
    new_string = ""
    for letter in string: 
        if ord(letter) == ord(old_char): 
            letter = new_char
        else: letter = letter 
        new_string += letter
        
    return new_string


def get_nb_char(string: str, char: str) -> int:
    number_of_char = 0
    for letter in string:
        if ord(letter) == ord(char):
            number_of_char += 1
        else: number_of_char += 0
    return number_of_char


def get_nb_words(sentence: str) -> int:
    number_of_word = 1
    for letter in sentence:
        if ord(letter) == 32:
            number_of_word += 1
        else: number_of_word += 0
    return number_of_word


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
