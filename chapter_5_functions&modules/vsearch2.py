
##
##def search4vowels(word):
##    """ Searches for the vowels in an
##    entered string. """
##    vowels = set('aeiou')
##    ##    word = input('Provide a word to search for vowels: ')
##    found = vowels.intersection(set(word))
##    for vowel in sorted(found):
##        print(vowel)
##    return bool(found)


def search4vowels(phrase:str) -> set:
    """ Searches for the vowels in an
    entered string. """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letter(phrase:str='HelloWorld', letters:str='aeiou') -> set:
    """ Searches for the letters in a
    string. """
    return set(letters).intersection(set(phrase.lower()))
