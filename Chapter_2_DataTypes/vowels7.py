## Lists the number of vowels in a entered string

word = input("Seach for vowels in this word:>>>")
# Initialize the dictionary
vowels = set('aeiou')

# Find the common elements between the sets
found = vowels.intersection(set(word))
        
# Print the set results sorted    
for vowel in sorted(found):
    print( vowel, 'was found')
