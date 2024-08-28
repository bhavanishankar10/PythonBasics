# DATE - 28/8/24

# Tuples
    # eg 1

items = (1,"apple",2,"banana")  # () -> used to store tuple values
print(items)
print(items[1])     # accessing specific values of tuple
print(items[-1])    # -ve indexing -> -1 = last item of tuple
print(items[0:2])   # accessing values using range
if "apple" in items:    # in checks for item/value in tuple
    print("Yes , 'apple' is present in tuple")

# since tuples are immutable , we cannot change/add/remove values in tuple
# instead we convert tuple -> list , change/add/remove values, then convert back list -> tuple

items_list = list(items)    # tuple -> list
print(items_list)   # list
items_list1 = [3,"mango"]   
items_list.extend(items_list1)  # .extend()
print(items_list)
items = tuple(items_list)   # list -> tuple
print(items)    # tuple

for x in items:         # for loop
    print(x,end=' ')

print()
i = 0                   # while loop
while i<len(items):     
    print(items[i],end=' ')
    i += 1

# we can concatenate 2 tuples using  "+" operator 