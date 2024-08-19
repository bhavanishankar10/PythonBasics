# DATE - 17/8/24 , SATURDAY

# String  Concepts

name = "elon musk"   # String -> array of char ; string characters are indexed from 0,1,2 ....n
print(name[2],"\n")      # variable_name[] helps to get a specific character from string

#for x in name:
    #print(x)

print("length of name = ", len(name))  # length of string

print("Musk" in name) # in checks for specific phrase/char in string "musk"->TRUE, "Musk"->FALSE -                          case senisitve

a = "slicing string"    # String Slicing 
print(a[6:13])
print(a[1:])    # Slicing to the End
print(a[:10])   # Slicing from Start

print("Reverse string : " , a[::-1])    # No built-in func for reverse string in python
                                        # we use var_name[::1] to reverse a string

# eg 2
name = "abcdefgh"

print(name[:])
print(name[::])
print(name[0:])
print(name[1:])
print(name[0:5])
print(name[:8])
print(name[0:7])

replaceString = "ran inside"    # .replace() used to replace a specified string/char
print(replaceString.replace("n","l"))

print(replaceString.split(" "))   # .split() returns a string as a List of items, items ->separated by separator


    # format strings -> to concatenate strings & number
# eg1
age = 18
name = "rahul"
details = name + " is {} years old"     # {} -> placeholder should be in '' or ""
                                        # else TypeError -> str + int can't concatenate
print(details.format(age))    # var_name.format(var) -> combines number & string with help of {}placeholder

# eg2
bats = 5
balls = 8
glove_pair = 7
shop = "There are {0} bats , {1} balls & {2} glovePairs available in shop ." #{} can hold index num as well
print(shop.format(bats,balls,glove_pair))   # .format() -> can hold multiple arguments identified with
                                            # with index number

# f-strings (string formatting)
fruits = 3
vegetables = 6
dryFruits = 2
storeName = "Dmart"
grocery = f"There are {fruits} varities of fruits , {vegetables} varieties of vegetables & {dryFruits} varieties of dry fruits in {storeName} ."     # f is used here infront of a string literal & {value} used as placeholders.
print(grocery)                      # With f strings {} cannot be empty !!