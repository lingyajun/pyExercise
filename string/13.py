def user_input():
    msg = input('please input you words: ')
    return msg.lower(), msg.upper()

#print(user_input())
a, b = user_input()
print(a, b)
