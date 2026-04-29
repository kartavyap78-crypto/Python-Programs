# 19. Write a program where a user enters the buying price and selling price, then the output should show if the person has made a profit or loss.
# Example:
# •	Buy = 400
# •	Sell = 600
# •	Output: The User has made a profit

buy = int(input("enter a buy price = "))
sell = int(input("enter a sell price = "))

if sell > buy:
    print("the user made a profit")
else:
    print("the user made a loss")