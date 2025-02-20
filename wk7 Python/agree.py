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


if agree in ["Y", "y", "YES", "yes","Yes"]:
    print("Agreed.")
elif agree in ["N", "n", "NO", "no", "No"]:
    print("Not Agreed.")


agree = agree.lower()
if agree in ["yes", "y"]:
    print("Agreed.")
elif agree in ["no", "n"]:
    print("Not Agreed.")

