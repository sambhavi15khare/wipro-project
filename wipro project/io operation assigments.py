# IO Operations Hands-on Assignment 1

file = open("sample.txt", "r")
print(file.read())
file.close()


# IO Operations Hands-on Assignment 2

n = int(input("Enter number of lines: "))

file = open("sample.txt", "r")
for i in range(n):
    line = file.readline()
    if line == "":
        break
    print(line, end="")
file.close()


# IO Operations Hands-on Assignment 3

text = input("Enter text to append: ")

file = open("sample.txt", "a")
file.write("\n" + text)
file.close()

print("Data appended successfully.")


# IO Operations Hands-on Assignment 4

file = open("sample.txt", "r")
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines]

print(lines)


# IO Operations Hands-on Assignment 5

file = open("sample.txt", "r")
text = file.read()
file.close()

words = text.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)


# IO Operations Hands-on Assignment 6

word = input("Enter word to search: ").lower()

file = open("sample.txt", "r")
text = file.read().lower()
file.close()

words = text.split()

count = words.count(word)

print("Frequency:", count)
