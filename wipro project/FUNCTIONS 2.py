# Project 2

def ispalindrome(name):
    if name == name[::-1]:
        return "Yes, it is a palindrome."
    else:
        return "No, it is not a palindrome."


def count_the_vowels(name):
    count = 0

    for ch in name.lower():
        if ch in "aeiou":
            count += 1

    return count


def frequency_of_letters(name):
    frequency = {}

    for ch in name:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    return frequency


name = input("Enter a string: ")

print(ispalindrome(name))
print("Number of vowels:", count_the_vowels(name))

print("Frequency of letters:")
result = frequency_of_letters(name)

for key in result:
    print(key, ":", result[key])
