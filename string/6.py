def appending(s):
    if len(s) < 3 :
        return s
    if s.endswith('ing'):
        s = s + 'ly'
    else:
        s = s + 'ing'
    return s

print( appending('abc'))
print( appending('string'))
