def first(n):
    return n[0]
def last(n):
    return n[-1]

def sort_list(items):
#    return items.sort()
#    return sorted(items)
    return sorted(items, key=last)

items =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_list(items))
