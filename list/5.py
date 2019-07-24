def count(items):
    num = 0
    for s in items:
        length = len(s)
        if length == 2 or \
            (length>2 and s[0]==s[length -1]):
            num +=1
    return num

items = ['abc', 'xyz', 'aba', '1221']
print(count(items))
