#!/usr/bin/python3
import re

text_example = "hey hello welcome this is 123 \tRJ"

# To find matching Digits with \d in text (for not Digit you can use \D) 
digit_pattern = re.compile(r"\d")
#digit_pattern = re.compile(r"\D")

matches = digit_pattern.finditer(text_example)
print("To find the digits using \\d")
for i in matches:
    print(i)
print("-----------------------------")

# To find whitespaces chars in text \s (opposite to this is \S)

space_pattern = re.compile(r"\s")
#space_pattern = re.compile(r"\S")

space_match = space_pattern.finditer(text_example)
print("To find whitespaces chars in text \\s")
for i in space_match:
    print(i)
print("------------------------------")

# To find alpha numeric chars in text \w (opposite to this is \W)

alpha_numeric_pattern = re.compile(r"\w")
#alpha_numeric_pattern = re.compile(r"\W")

char_match = alpha_numeric_pattern.finditer(text_example)
print("To find alpha numeric chars in text \\w")
for i in char_match:
    print(i)
print("------------------------------")

# To find the beginning of a block of text [space is the delimiter] \b (opposite to this is \B )

beginning = re.compile(r"\bhello")
#beginning = re.compile(r"\Blo")
beginning_match = beginning.finditer(text_example)

print("To find the beginning of a block of text [space is the delimiter] \\b")
for i in beginning_match:
    print(i)

