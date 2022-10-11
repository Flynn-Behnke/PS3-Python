name = str(input("Enter last name "))
depend = float(input("Enter number of dependents "))
ginc = float(input("Enter gross income "))

aginc = ginc-(depend*12000)
if aginc<=50000:
  rate = 0.1
else:
  rate = 0.2
  
tax = rate*aginc
if tax<0:
  inctax=100
else:
  inctax=tax

print(name, "number of dependents is", depend, "gross income is", ginc, "adjusted gross income is", aginc, "and income tax is", inctax)
