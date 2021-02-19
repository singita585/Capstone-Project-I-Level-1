import math 
calculation = input('''Choose either 'investment' or 'bond' from the menu below to proceed:

investment - to calculate the amount of interest you'll earn on interest.
bond - to calculate the amount you'll have to pay on a home loan \n\n''')

if calculation == calculation.capitalize() or calculation == calculation.upper() or calculation == calculation.lower():
  print("Valid")
else:
  print("Invalid")

if calculation == "investment" or calculation == "Investment" or calculation == "INVESTMENT":		#if the user choose investment this is how we calculate.
  deposit = float(input("How much are you depositing."))
  interest_rate = int(input("Enter the interest rate."))
  years = int(input("Enter the number of years are you planning to invest."))
  interest = input("Choose whether you want simple interest or compound interest.")

  print(deposit)
  print(interest_rate)
  print(years)
  print(interest)

  if interest == "simple interest":																	# Calculation if the user choose simple interest
    simple_total_amount = deposit*(1+interest_rate/100*years)
  print(simple_total_amount)

  if interest == "compound interest":																	# Calculation if the user choose compound interest
    compound_total_amount = deposit*math.pow((1+interest_rate),years)
  print(compound_total_amount)

elif calculation == "bond" or calculation =="BOND" or calculation == "Bond":                         #if the user choose bond this is how we calculate.
  present_value = int(input("Enter the current amount of your house"))
  bond_interest_rate = int(input("Enter the interest rate"))
  months = int(input("Enter the number of months you plan to take to repay the bond"))

  print(present_value)
  print(bond_interest_rate)
  print(months)

  home_loans = round((bond_interest_rate/12*present_value)/(1-(1+bond_interest_rate/12)**(-months)))
  print(home_loans)
  