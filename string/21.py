def uppers(msg):
    sum = 0
    for c in msg[:4]:
        if c.upper() == c:
            sum+=1
    if sum > 1:
        return msg.upper()
    return msg

print( uppers('OOuppers'))
print( uppers('OkkkkIOuppers'))
print( uppers('Ouppers'))
