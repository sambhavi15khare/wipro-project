# Assignment 1

import sys

print("File Name:", sys.argv[0])
print("Arguments:", sys.argv[1:])


# Assignment 2

import sys

sum = 0

for i in sys.argv[1:]:
    sum += int(i)

print("Sum =", sum)


# Assignment 3

import sys

if len(sys.argv) < 2:
    print("No arguments given")
else:
    for i in sys.argv[1:]:
        print(i, end=" ")
