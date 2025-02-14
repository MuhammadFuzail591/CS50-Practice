def info(name, age):
    print(f"Your Name is {name} and you are {age} years old")

# Positional Parameters
info("Fuzail",21)

# Named Parameters
info(name="Muhammad Fuzail", age=21);


#Default Parameters
def info2(name, age=20):
    print(f"Your name is {name} and your age is {age} years");

info2("Ali hamza");

#Arbitrary parameters
def arbitraryValues(*args):
    total = 0
    for value in args:
        total+=value
    return total

print(arbitraryValues(1,2,2,3,45,3));
print(arbitraryValues(3,4,5))


# Arbitrary Keyword Arguments
def display_info(**kwrgs):
    for key, value in kwrgs.items():
        print(f"{key} : {value}")

display_info(name = "Ali", age=21, city = "Sargodha");

