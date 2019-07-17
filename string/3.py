def str_head_tail(s):
    length = len(s)
    if length < 2:
        return ''
 #   return s[0:2] + s[length -2 : ]
    return s[0:2] + s[ -2 : ]

print(str_head_tail('w3resource'))
print(str_head_tail('dc'))
print(str_head_tail('dcf'))
print(str_head_tail('c'))
