import sys

like = list(map(int, sys.argv[1].split("-")))
dislike = list(map(int, sys.argv[2].split("-")))
numbers = list(map(int, sys.argv[3].split("-")))

happiness = 0

for num in numbers:
    if num in like:
        happiness += 1
    elif num in dislike:
        happiness -= 1

print(happiness)
