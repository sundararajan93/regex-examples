#!/usr/bin/python3
import re

text_string = "This is a sample string with IP address 192.168.1.7"

pattern = re.compile(r'[0-9][0-9][0-9]\.')

extract = pattern.findall(text_string)
print(extract)