item = str(input("Enter item "))
quantity = float(input("Enter quantity "))
if item=="A":
  up=10.00
else:
  up=20.00

extprice = up*quantity

print("The item is ", item, "the extended price is ", extprice)
