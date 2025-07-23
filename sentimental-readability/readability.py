from cs50 import get_string

# getting the sentence
text = get_string("Text: ")

# length of text
strlength = len(text)
p
# variable declaration
j = 0
i = 0
k = 0

letternumber = 0
wordnumber = 0
spaces = 0
sentence = 0

# counting letters
while j < strlength:
    if text[j].isalpha():
        letternumber = letternumber + 1
    j = j + 1

# counting words
while i < strlength:
    if text[i].isspace():
        spaces = spaces + 1
    i = i + 1
wordnumber = spaces + 1

# counting sentences
while k < strlength:
    if text[k] == "." or text[k] == "?" or text[k] == "!":
        sentence = sentence + 1
    k = k + 1

# applying formula
formula = (0.0588 * letternumber / wordnumber * 100) - (0.296 * sentence / wordnumber * 100) - 15.8
lvl = (round(formula))

# printing
if lvl >= 16:
    print("Grade 16+")

if lvl < 1:
    print("Before Grade 1")

if lvl >= 1 and lvl < 16:
    print("Grade", lvl)
