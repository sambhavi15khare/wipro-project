# Assignment 1

def sum_list(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

numbers = [8, 2, 3, 0, 7]
print("Sum =", sum_list(numbers))


# Assignment 2

def reverse_string(text):
    return text[::-1]

text = input("Enter a string: ")
print("Reversed String:", reverse_string(text))


# Assignment 3

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))


# Assignment 4

def count_case(text):
    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("Upper Case Letters :", upper)
    print("Lower Case Letters :", lower)

text = input("Enter a string: ")
count_case(text)


# Assignment 5

def unique_list(lst):
    unique = []

    for i in lst:
        if i not in unique:
            unique.append(i)

    return unique

numbers = [1,2,3,3,3,3,4,5]
print("Unique List:", unique_list(numbers))


# Assignment 6

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print("Prime Number")
else:
    print("Not a Prime Number")
