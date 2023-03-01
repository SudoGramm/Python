print("Hello and welcome to CC Jitters!")

name = input("What is your name?: ")

print("Hello " + name + ", what would you like from the menu\n")

order = input("Latte 2.00$\n" + "Hot Chocolate 2.00$\n" + "Espresso 2.00$ : \n")

espresso = "2.00"

latte = "2.00"

hot_chocolate = "2.00"

print("Ok! Your " + order + " will be ready in a few minutes!")

extra = input("While you're waiting would you like anything else by\nany chance?: \n")

if extra == "no":
  print("Okay your " + order + " is done!\n")
else:
  print("Ok, your " + extra + " will be ready in a few minutes too!\n" + "Your orders are ready!\n")

if extra == "no":
  print("Your total is 2.00$.")
else:
  print("Your total is 4.00$")

  



  


