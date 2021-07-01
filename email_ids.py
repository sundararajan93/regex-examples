#!/usr/bin/python3

import re
import urllib.request


URL = 'https://www.digitalgyd.com/email-name-ideas/'
open_url = urllib.request.urlopen(URL)
html = open_url.read()

mystr = html.decode("utf8")
open_url.close()

text = mystr

email_pattern = re.compile(r"([a-zA-Z0-9-_.]+)@([a-zA-Z0-9-]+)\.([a-zA-Z-]+)")
matches = email_pattern.finditer(text)

for i in matches:
    print(i.group())

# sample_text = """
# Email can be very useful for messages that have slightly more content than a text sundararajan.t1@gmail.com message, 
# but it is still best used for fairly brief messages. Many businesses use automated emails to 
# acknowledge communications from the public, or to remind associates that periodic geeksundar@yahoo.com reports or payments 
# are due. You may also be assigned to “populate” a form email in which standard paragraphs 
# are used but you choose from a menu of sentences to make the Shannon@just-engaged.com or Chris@Lailasman.com wording suitable for presilla@hotmail.net a particular transaction.
# """


# email_pattern = re.compile(r"([a-zA-Z0-9-_.]+)@([a-zA-Z0-9-]+)\.([a-zA-Z-]+)")
# matches = email_pattern.finditer(html)

# for i in matches:
#     print(i.group())

# By default group(0) - Display all the values
# since we grouped as three (....)@(....).(....) we can call with respective numbers
# group(1) -> mailid -> sundararajan.t1
# group(2) -> Domain -> gmail
# group(2) -> Extension -> com
