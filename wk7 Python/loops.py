# while loop repeats a block of code as long as a condition is True
i = 0
while i < 3:
    print("while loop")
    i += 1

while True:
    inp = input("Enter quit to exit: ")
    if(inp == "quit"):
        break;
    print(f"You entered {inp}")

#for loop is commonly used for iteration over a sequence and execute a block of code for each item

for i in [0,1,2]:
    print(f"for loop and value is {i}")

#for loop with range

for i in range(3):
    print(f"for loop with range and value is {i}")

#for loop best practice/ industry standard

for _ in range(3):
    print(f"for loop with range and _")

#for loop iterating over the letters of word

word = "python"
for letter in word:
    print(letter)

#for loop iteration over the list
fruits = ["banana","apple","cherry"]
for fruit in fruits:
    print(fruit)