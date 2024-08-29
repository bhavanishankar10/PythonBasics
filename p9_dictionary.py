# DATE - 29/8/24

# Dictionaries
    # eg 1

items = {1:"apple" , "banana":2 , 3:[1,"a",2,"b"]}
print(items)    # key -> only immutable datatype ; values -> can be of any datatype 

print("Accessed value - ",items[3]) # dict_name[key_name] -> can access specified value

print()
print(items.keys()) # dict_name.keys() -> returns list of all keys in dictionary
print(items.values()) # dict_name.values() -> returns all values in dictionary

print()
if "car" in items:  # "in" checks for the presence of "key" in dictionary
    print("Key - car is present in dict")
else:
    print("Key - car not present in dict")

print()
items[1] = "mango"    # dict_name[key_name] = new_val -> changes value of specified key
print(items)

print()
items["orange"] = 5 # dict_name[new_key] = new_val -> adds new key-value pair to dict
print(items)

print()
items.pop("orange")  # dict_name.pop(key_name) -> removes specified item with given key
print(items)

        # for loop
print()
for x in items:  # returns keys of dict
    print(x,end=' ')
print()
for x in items:
    print(items[x],end=' ') #return values of dict

# other alternative to retrieve keys/values using for loop :-
    # for x in items.keys():
        # print(x)
    # for x in items.values():
        # print(x)

print("\n")
items1 = items.copy()   # new_dict = old_dict.copy() -> copies all items of old to new
print("Copy of old dict items : ",items1)