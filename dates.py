#!/usr/bin/python3
import re

dates = """
01.04.2021
01.01.2020

2021.04.01

2021-04-01
2021-04-29
2021-08-18
2021-09-13
2021-12-20

2021/11/25
2021/02/27
2021/03/23

2021_05_17
"""

# Finding YYYYMMDD format
yyyy_mm_dd = re.compile(r"\d\d\d\d.\d\d.\d\d")
matches = yyyy_mm_dd.finditer(dates)

for date in matches:
    print(date)

# Finding YYYYMMDD in a particular format [example: yyyy/mm/dd]

#pattern2 = re.compile(r"\d\d\d\d[/]\d\d[/]\d\d")
#pattern2 = re.compile(r"\d{4}[-/]\d{2}[-/]\d{2}")
pattern2 = re.compile(r"\d{2}\.\d{2}\.\d{4}")
matches2 = pattern2.finditer(dates)
print("--------------------------")
for date in matches2:
    print(date)