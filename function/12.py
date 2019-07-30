def check_palindrome(msg):
    r = True
    size = len(msg)
    maxRange = int(size/2+1)
    for i in range(maxRange):
        if msg[i] != msg[size-i-1]:
            r = False
            break
    print(msg, size, maxRange)
    return r

print(check_palindrome('abc'),check_palindrome('abccba'),check_palindrome('12321'))
print(check_palindrome('c'),check_palindrome('ab'))
print(check_palindrome('Madam'))
