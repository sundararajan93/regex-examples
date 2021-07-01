#!/usr/bin/python3

import re

text_pattern = "123asdf45346abc2344ABCaabc"

# methods 
# 1. finditer()

pattern = re.compile(r"abc")
matches = pattern.finditer(text_pattern)

# Another simplest way to perform finditer
# matches = re.finditer(r"abc", text_pattern)

print("finditer() method")
for i in matches:
    print(i)
print("--------------------")
for i in matches:
    print(i.span())
# 2. findall() - To just print the match strings

find_all_example = pattern.findall(text_pattern)
print("findall() method")
for i in find_all_example:
    print(i)
print("--------------------")

# 3. match() - return only one match (the match look only from the beginning of the text)
print("match() method")
match_example = pattern.match(text_pattern)
print(match_example)
print("---------------------")

# 4. search() - search and return the first match
print("search() method")
search_example = pattern.search(text_pattern)
print(search_example)
print("---------------------")

# Getting span values with span(), start(), end()
print("getting span, start , end values")
span_example = pattern.finditer(text_pattern)
for i in span_example:
    print(i.span(), i.start(), i.end())