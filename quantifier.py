#!/usr/bin/python3
import re

text = "A sample string 234_23 for just a regex string structure"

# To find 0 or more char matching pattern [If there is no match it returns blank]
#pattern = re.compile(r"\d*") 

# To find 1 or more char matching pattern only will be displayed
#pattern = re.compile(r"\d+")

# To use optional ?_ means _ is optional [show if pattern with _ there else skip]
#pattern = re.compile(r"\d?_")

# To use a pattern {3} - To display three digits/char, {1,3} To display if text has 123 {start, end}
#pattern = re.compile(r"_\d{2}")
#pattern = re.compile(r"\d{3}")
pattern = re.compile(r"\w[string]{5}")


matches = pattern.findall(text)

for i in matches:
    print(i)