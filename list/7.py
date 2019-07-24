def remove_duplicates(items):
    s = set(items)
    return list(s)

items = [1,2,2,3,3,3,5]
print(remove_duplicates(items))
