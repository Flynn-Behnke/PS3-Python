books = float(input("Enter amount of books to be ordered "))
price = float(input("Enter price of each book "))

cost = books*price

if cost<=50:
  ship=25
else:
  ship=0

total=cost+ship

print("The total is ", total, "and shipping cost of ", ship)
