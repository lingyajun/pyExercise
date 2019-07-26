from itertools import combinations

def sub_list(mlist):
    subs = list()
    all_list = list()
    for i in range(1+len(mlist)):
        t0 = [list(x)  for x in combinations(mlist, i)]
        if len(t0) > 0:
            subs.extend(t0)
            all_list.append(t0)    
    return subs,all_list

mlist = [1,2,3,4]
subs,all_list = sub_list(mlist)
print(subs)
print()
print(all_list)

