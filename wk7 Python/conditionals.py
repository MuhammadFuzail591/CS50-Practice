x= int(input("x: "))
y= int(input("y: "))

print(x + y)

if x < y : 
    print("x is less than y")


# if else
if x < y:
    print("x is less than y")
else:
    print("x is not less than y")


#if else if

if(x<y):
    print("x is less than y")
elif(x<10):
    print("x is less than 10")
elif(y<10):
    print("y is less than 10")
else:
    print("x is not less than y")


s = input("s: ")
t = input("t: ")

if(s == t):
    print("same")
else:
    print("Not same")

agree = input("Are You Agree.? ")

if agree == "Y" or agree == "y":
    print("Agreed.")
elif agree == "N" or agree == "n":
    print("Not Agreed.")


#Better Code same logic
if agree in ["Y", "y"]:
    print("Agreed.")
elif agree in ["N", "n"]:
    print("Not Agreed.")