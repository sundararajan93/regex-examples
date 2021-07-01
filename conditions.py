#!/usr/bin/python3
import re

string_text = """
Mr Simpson
Mrs Simpson
Mr. Smith
Mrs Bronson did this
Mr. T
Ms Praveena
Hello
how
are youy
127.0.50.54
abacasf
State
"""

# To filter out only names from the string 
pattern = re.compile(r"(Mr|Mrs|Ms)\.?\s\w+")

matches = pattern.finditer(string_text)

for i in matches:
    print(i)