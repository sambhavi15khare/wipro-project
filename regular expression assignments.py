# Assignment 1

import re

strings = ['789', '123', '004']

for s in strings:
    if re.fullmatch(r'[0-7]+', s):
        print(s, "-> Octal")
    else:
        print(s, "-> Not Octal")


# Assignment 2

import re

emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

pattern = r'(\w+)@(\w+)\.(\w+)'

matches = re.findall(pattern, emails)

for userid, domain, suffix in matches:
    print("User ID :", userid)
    print("Domain  :", domain)
    print("Suffix  :", suffix)
    print()


# Assignment 3

import re

sentence = "A, very   very; irregular_sentence"

sentence = re.sub(r'[_,;]', ' ', sentence)
sentence = re.sub(r'\s+', ' ', sentence)

print(sentence.strip())


# Assignment 4

import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

tweet = re.sub(r'http\S+', '', tweet)
tweet = re.sub(r'@\w+', '', tweet)
tweet = re.sub(r'#\w+', '', tweet)
tweet = re.sub(r'\bRT\b', '', tweet)
tweet = re.sub(r'\bcc\b:?', '', tweet)
tweet = re.sub(r'[^\w\s]', '', tweet)
tweet = re.sub(r'\s+', ' ', tweet)

print(tweet.strip())


# Assignment 5

import requests
import re

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text

result = re.findall(r'>([^<>]+)<', html)

result = [text.strip() for text in result if text.strip()]

print(result)


# Assignment 6

import re

words = [
    "civic",
    "trust",
    "widows",
    "maximum",
    "museums",
    "aa"
]

for word in words:
    if re.fullmatch(r'(.).*\1', word):
        print(word)
