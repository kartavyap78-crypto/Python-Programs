# 25. Accept the marked price from the user and calculate the net amount to pay according to the following criteria:
# Marked Price	Discount
# > 10,000	20%
# > 7,000 and <= 10,000	15%
# >= 7,000	10%

market_price = int(input("enter the market price = "))

if market_price > 10000:
    discount = market_price * 20/100
    print("dicount price = ",discount)
  
elif market_price > 7000 and market_price <= 10000:
    discount = market_price * 15/100
    print("discount price = ",discount)
    
elif market_price >= 5000:
    discount = market_price * 10/100
    print("discount price = ",discount)
    
else:
    print("invalid")


print(market_price-discount)