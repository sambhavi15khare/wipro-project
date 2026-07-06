file = open("sample.txt", "r")

lines = file.readlines()
line_count = len(lines)

if line_count > 12:
    if line_count == 24:
        time = 12
    else:
        time = line_count - 12
    period = "PM"
else:
    time = line_count
    period = "AM"

words = []

for line in lines:
    line = line.lower()
    for ch in ",.!?;:-()[]{}\"'":
        line = line.replace(ch, " ")
    words.extend(line.split())

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

place = max(frequency, key=frequency.get)

print("Meeting time:", time, period)
print("Meeting place:", place.capitalize(), "Street")

file.close()
