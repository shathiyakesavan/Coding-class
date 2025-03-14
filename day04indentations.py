# #an if statement tells python to do something only if a condition is true
# age = 29
# if age >= 18:
#   print("You can vote")
# else:
#   print("You can't vote")
# sellingprice = 120

# if sellingprice >= 100:
#     print("The profit is positive", sellingprice - 100)
# else:
#     print("Your profit is negative", )
# buyingprice = float(input("please enter the buying price"))
# sellingprice = float(input("Please enter the selling price"))
# if buyingprice > sellingprice:
#     print("It is a loss")
# elif buyingprice == sellingprice:
#     print("It is not a profit or loss")
# else: 
#     print("It is a profit")

number1 = int(input("Please enter number"))
number2 = int(input("Please enter number"))
number3 = int(input("Please enter number"))
if number1 > number2 and number1 > number3:
    print("number 1")
elif number2 > number1 and number2 > number3:
    print("number 2")
else:
    print("number 3")
 