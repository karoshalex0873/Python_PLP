def calculate_discount(price, discount_percent):
  if discount_percent>=20:
    discount=(discount_percent/100)*price
    print("You have a dicount of: ",discount)
  else:
    discount=0
    print("The commodity is not eligble for the discount")
  TotalCost=price-discount
  print("The TotalCost of the commodity is ",TotalCost)

def userinput():
  price=int(input("Enter the price of commodity: "))
  discount_percent=int(input("Enter the  discount for calculation: "))
  calculate_discount(price, discount_percent)

userinput()