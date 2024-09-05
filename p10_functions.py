# DATE - 5/9/24

# Functions 

# eg 1
def func():
    print("This is 1st function program\n")
func()

# eg 2  Arguments passing
def func1(name,age):    # 2 parameters - name ,age
    print("Hey my name is "+name+" & I am "+str(age)+" years old.\n")
func1("Rahul",24)       # 2 arguments - Rahul , 24

# eg 2.1  ( alternative to eg 2 )
def func1_1(*details):
    print("Hey my name is "+details[0]+" & I am "+str(details[1])+" years old.\n")
func1_1("Charan",18)

# eg 3  Arbitrary arguments i.e  *args
def func2(*fruits):     
    print("These are the fruits I like : "+str(fruits)+"\n")
    
    print("These are the fruits I like : " )
    for x in fruits:    # using for loop
        print(x,end=' ')

    print()
    print("Most liked one is : "+fruits[1]) # accessing value from tuple
func2("apple","mango","banana")     # IMPORTANT -> arguments are sent in the form of tuple

print()
# eg 4 Key-word arguments 
def func3(animal1 , animal2 , animal3):
    print("The largest animal is : " + animal3)
    print("The other 2 animals "+animal1+" & "+animal2+" are small.\n")
func3(animal1 = 'cat' , animal2 = 'dog' , animal3 = 'elephant') # key-word arguments are sent
                                                                # in the form of dictionary

# eg 4.1 Arbitrary Key-word arguments i.e **kwargs
def func3_1(**animals):
    print("The largest animal is : " + animals['animal3'])  # parameter[key]
    print("The other 2 animals "+animals['animal1']+" & "+animals['animal2']+" are small.\n")
func3_1(animal1 = 'tiger' , animal2 = 'lion' , animal3 = 'hippo')

# eg 5
def car_brand(cars):
    for x in cars:
        print(x,end=' ')
car = ['Honda','Hyundai','Kia','Tata']  # passing list as arguments into function
car_brand(car)               # we can pass any datatypes in function number,list,tuple,set,etc...
