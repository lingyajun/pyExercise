def exchange_str(s1, s2):
    if (len(s1) < 2) or (len(s2) < 2):
        return ''
    c1, c2 = s1[0:2], s2[0:2]
    s1 = s1.replace(c1, c2)
    s2 = s2.replace(c2, c1)
    return s1+ ' ' +s2

print(exchange_str('abc', 'xyz'))

def exchange_str2(s1, s2):
    if (len(s1) < 2) or (len(s2) < 2):
        return ''
    ns1 = s2[:2] + s1[2:]
    ns2 = s1[:2] + s2[2:]
    return ns1+ ' ' +ns2

print(exchange_str2('ab-c', 'xy.z'))

