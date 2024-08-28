# DATE  - 28/8/24

# Sets
    # eg 1

items = {1,"apple",2,"banana"}
print(items)     # set items -> unordered => hence output is always changing
    # can't access set items with index -> because it is unordered 

for x in items:
    print(x)

print()
if "apple" in items:
    print("apple is present in item set")

    # set items are immutable - can't be changed , but we can add/remove items in set

print()
items.add(3)    # set_name.add(val) -> adds new item to set
print(items)
    
print()
items1 = {"mango",4}
items.update(items1)    # old_set.update(new_set) -> adds items of new_set to old_set
print(items)

print()
items.remove(4)     # set_name.remove(val) -> removes item from set
print(items)        # other alternative to remove -> set_name.discard(val)

