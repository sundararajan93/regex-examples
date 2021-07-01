#!/usr/bin/python3

import re

text_pattern = "123asdf45346abc2344ABCaabc."
pattern = re.compile(r".")
matches = pattern.finditer(text_pattern)

print(". - to print all the pattern except newline")
for i in matches:
    print(i.group())

print("To print the actual . you can escape with \\")
dot = re.compile(r"\.")
find_dot = dot.finditer(text_pattern)
for i in find_dot:
    print(i.group())

print("To find match in start of the text")
start_with = re.compile("^123")
find_start_match = start_with.finditer(text_pattern)

for i in find_start_match:
    print(i)

print("To find the word ends with a pattern of text")
text_new = "Kumar Singh"
text_pattern_new = re.compile("Singh$")
find_end_match = text_pattern_new.findall(text_new)

for i in find_end_match:
    print(i)