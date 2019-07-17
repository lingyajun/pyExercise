def change_char(s):
    c0 = s[0]
    s2 = s[1:]
    s2 = s2.replace(c0, '$')
    s = c0 + s2
    return s

print(change_char('restart'))
