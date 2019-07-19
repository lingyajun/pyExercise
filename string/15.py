def add_tags(tag, msg):
    return f'<{tag}>{msg}</{tag}>'
    # return '<'+tag+'>' + 

print(add_tags('i','python'))
