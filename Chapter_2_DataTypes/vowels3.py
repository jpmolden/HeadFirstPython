## Lists the number of vowels in a entered string

word = input("Seach for vowels in this word:>>>")
# Initialize the dictionary
found = { 'a':0, 'e':0, 'i':0, 'o':0, 'u':0 }

# Iterate over each letter in the entered string
for letter in word:
    if letter in found:
        found[letter] += 1

# Print the dictionary results sorted in key order     
for k, v in sorted(found.items()):
    print( k, 'was found',v , 'times(s).')
