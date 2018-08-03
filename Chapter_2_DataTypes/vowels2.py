

# Lists (literal)
# list of lists

odds_and_ends = [ [1, 2, 3], ['a','b','c'], [1.1, 1.2, 34.5]]


word = input("Seach for vowels in this word:>>>")
vowels = ['a', 'e','i','o','u']
found = []

for letter in word:
    if letter in vowels:
            if letter not in found:
                found.append(letter)

for vowel in found:
    print(vowel)

nums = [1,2,3,4]
print(nums)
# pop the fist object in the list
nums.pop(0)
