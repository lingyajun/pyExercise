import re

def is_characters(msg):
    pattern = re.compile(r'[^a-zA-Z0-9]')
    s = pattern.search(msg)
    print(msg, s, sep='  =  ')
    return not bool(s)

r = is_characters('ABCDEFabcdef123450')
print(r)
r = is_characters("*&%@#!}{")
print(r)

