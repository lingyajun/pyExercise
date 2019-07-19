def last_str(c, msg):
    index = msg.rfind(c)
    if index > 0:
        return msg[:index]
      #  return msg[index+1:]#
    else:
        return msg

print(last_str('/','https://www.w3resource.com/python-exercises/tag'))
print(last_str('-','https://www.w3resource.com/python-exercises/tag'))
print(last_str('/','/python/'))
