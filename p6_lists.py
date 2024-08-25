
# 25/8/24

# Lists
    # eg 1
items = [1,"apple",2,"banana",3,"mango"]
print(items[2])
print(items[-1])    # -ve indexing -> starts from end ; -1 = last item index
print(items[0:3])   # items displayed in the form of list using range 
if 2 in items:      # in checks for value/item in the list
    print("2 exists in item list")

items[3] = "lemon"  # list[index] = new_value -> changes specific value in list
print(items)
items[1:4] = ["melon",5,"almond"]   # changes range of values
print(items)

items.insert(6,4)   # .insert(index , new_value) -> inserts value at specified index
print(items)        # without replacing existing values
items.append("cherry")      # .append(new_val) -> appends item at end of list
print(items)

items1 = [5,"orange",6]
items.extend(items1)    # old_list.extend(new_list) -> appends new_list to old_list
print(items)

items.remove("orange")  # list.remove(item) -> removes specified "item" from list
print(items)
items.pop(9)            # list.pop(index) -> removes specified "index" from list
print(items)


for x in items:         # list for loop
    print(x,end=' ')

print()
i = 0
while i < len(items):    # list while loop
    print(items[i],end=' ')
    i += 1

print()
copy_items = items.copy()   # new_list = old_list.copy() -> copies items from old->new list
print(copy_items)