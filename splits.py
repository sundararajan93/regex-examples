#!/usr/bin/python3
import re

text_sample = """
sundar:x:1000:1000:sundar,,,:/home/sundar:/bin/bash
"""

# split() to split the text with :
pattern = re.compile(r":")
split_string = pattern.split(text_sample)
print(split_string)

# Lets use sub() substitue : with -
sub_pattern = re.compile(r":")
sub_string = sub_pattern.sub("-", text_sample)
print(sub_string)
