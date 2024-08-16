# Variables , DataTypes concept

print("Hello world in Python")

a = 100
b = 120
print("Output = " , a+b)    # both are same dataType of int - we get output 

a = "100"
b = 120
#print("Output = " , a + b) => typeError for a+b - string can only concatenate with strings not int dataType
#typeError can be resolved using type converson methods
print("Type of a = " , type(a) ," and ", "Type of b = " , type(b))

a,b,c = 10,20,30    #assigning multiple values to multiple variables
print(a,b,c)

a=b=c="apple"   #assigning 1 value to multiple variables
print(a,b,c)


    # global , local variables
# eg1
global_var = "I am global"
def example():
    local_var = "I am local"
    print(global_var)   # Access global variable
    print(local_var)    # Access local variable

example()
#print(local_var)  # nameError: local_var is not accessible here

# eg2
x = "awesome"   # global variable (outside a function)
def myFunc():
    # global x   -> here we are converting a local variable into a global variable using "global" keyword
    # x = "fantastic"
    x = "fantastic"     #local variable (inside a function)
    print("Python is " + x)
#myFunc()
print("Python is " + x)
myFunc()

    # variable scope for outer-inner functions
def outer_function():
    outer_var = "I am outer"
    
    def inner_function():
        inner_var = "I am inner"
        print(outer_var)  # Can access outer_var
    
    inner_function()
    #print(inner_var)  # nameError: inner_var is not accessible here

outer_function()


    # unpacking variables
coordinates = (10, 20)
x, y = coordinates
print(x)  # 10
print(y)  # 20




