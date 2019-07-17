def char_frequency(str1):
    dict1 = {}
    for c in str1:
        keys = dict1.keys()
        if c in keys:
            continue
        else:
            dict1[c] = str1.count(c)
    return dict1

def char_frequency2(str1):
    dict1 = {}
    for c in str1:
        keys = dict1.keys()
        if c in keys:
            dict1[c] += 1
        else:
            dict1[c] = 1
    return dict1

print(char_frequency('google.com'))
print(char_frequency2('facebook.com'))

