def change_str(s):
   # length = len(s)
    ns = s[-1:] + s[1: -1] + s[:1]
    return ns

print(change_str('abcdefg'))
