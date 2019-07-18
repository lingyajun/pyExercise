def longest_word(words):
    longest = 0
    lword = ''
    for w in words:
        if len(w) > longest:
            longest = len(w)
            lword = w

    return lword

print(longest_word(['test', 'awarsome', 'pritice']))
