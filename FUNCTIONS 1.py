# Project 1

def sort_hyphen(words):
    word_list = words.split("-")
    word_list.sort()
    return "-".join(word_list)

colors = input("Enter hyphen-separated colors: ")

print("Sorted Colors:")
print(sort_hyphen(colors))
```
