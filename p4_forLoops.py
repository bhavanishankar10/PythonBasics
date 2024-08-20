# Loops 
    # for Loops

    #eg1
for x in "python":  # for var in sequence(string,list,tuple,range, etc..)
    print(x)
print("\n")

    # eg2
for i in [1,2,3,4,5]:
    print(i)
print("\n")

    # range() function
values = range(5)       # range -> buit-in function
for i in values:
    print(i)
print("\n")
    # eg2
for i in range(0, 10, 2):   # range(start,stop,step)
    print(i, end=" ")
print("\n")

    #eg3
items = ["apple","banana","chiku"]      # accessing items of list
for i in items:
    print(i)
print("\n")

    #eg 4.1 - for with else 
digits=[1,2,3,4,5]
for i in digits:
    print(i)
else:
    print("no digits left")
print("\n")
    
    #eg 4.2
digits = [1,2,3,4,5,6]
for i in digits:
    if i==5:break   # break will stop execution after condition is met
    print(i)
else:
    print("no digits left")
print("\n")

    #eg 5  Nested Loops
list1 = [1,2]
list2 = [3,4]
for i in list1:
    for j in list2:     # inner loop will execute 1 time for each iteration of outer loop
        print(i,j)
print("\n")

    #eg 6
for x in range(0,12,2):     #range(start,stop,step)
    print(x,end=' ')        # prints even numbers

print("\n")
    #eg 7
    # continue keyword
for x in range(1,10):
    if x==8:
        continue
    else:
        print(x,end=' ')

print("\n")

    # eg 8
num = [1,3,2,4,7,9]
max_value = max(num)     # max() -> gives max value in list
even_count,odd_count=0,0    # set count=0 since we don't know how many are even/odd
for i in num:
    if i%2==0:      # checks whether num in list is even/odd 
        even_count+=1
        print("The number "+str(i)+" is even")
    else:
        odd_count+=1
        print("The number "+str(i)+" is odd")
print("Even nums in list = " , even_count)
print("Odd nums in list = ",odd_count)
print("Max value in list = " ,max_value)

print("\n")
    # eg 8  -> generating random numbers in list
import random
num_list = random.sample(range(1,20),8)  # random.sample(range(1st,last),required) is built-in function
print("Random list : " ,num_list)         # prints 8 random numbers between 1 & 20 
even_count , odd_count = 0,0
for i in num_list :
    if i%2 == 0:
        print("The value "+ str(i)+" is  even")
        even_count +=1
    else :
        print("The value "+str(i)+" is odd")
        odd_count += 1
    
print("Even nums in list = " , even_count)
print("Odd nums in list " , odd_count)
print("Max value in list = " , max(num_list))