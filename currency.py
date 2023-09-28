money_amount = input("enter and amount of money you would like to have change made for: ")
decimal_amount=float(money_amount)
print(money_amount)

r_hundreds=round(decimal_amount%100,2)
hundreds=round((decimal_amount-r_hundreds)/100)

r_fifties=round(r_hundreds%50,2)
fifties=round((r_hundreds-r_fifties)/50)

r_twenties=round(r_fifties%20,2)
twenties=round((r_fifties-r_twenties)/20)

r_tens=round(r_twenties%10,2)
tens=round((r_twenties-r_tens)/10)

r_fives=round(r_tens%10,2)
fives=round((r_tens-r_fives)/5)

r_ones=round(r_fives%1,2)
ones=round((r_fives-r_ones)/1)

r_quarters=round(r_ones%.25,2)
quarters=round((r_ones-r_quarters)/.25)

r_dimes=round(r_quarters%.1,2)
dimes=round((r_quarters-r_dimes)/.1)

r_nickels=round(r_dimes%.05,2)
nickels=round((r_dimes-r_nickels)/.05)

r_pennies=round(r_nickels%.01,2)
pennies=round((r_nickels-r_pennies)/.01)







print("You need",hundreds,"$100 bills,")
print(fifties,"$50 bill(s),")
print(twenties,"$20 bill(s),")
print(tens,"$10 bill(s),")
print(fives,"$5 bill(s),")
print(ones,"$5 bill(s),")
print(quarters,"quarter(s),")
print(dimes,"dime(s),")
print(nickels,"nickel(s)")
print("and",pennies,"pennie(s).")
