name = str(input("Enter name of appliance "))
price = float(input("Enter price of appliance "))

if price<=1000:
  warranty=price*0.05
else:
  warranty=price*0.1

total = price+warranty

print(name, "price of appliance is", price, "the warranty costs", warranty, "and the total is", total)
