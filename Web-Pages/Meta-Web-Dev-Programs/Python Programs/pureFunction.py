num_list = [1,2,3,4,5]

def addList(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_num = addList(num_list, 6)

print(num_list)
print(new_num)