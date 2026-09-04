#Format Specifiers = {:flags}
#Format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = add plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12.34

#add dot then number for how many decimal (f is for floating point)
print("---Decimal---")
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.0f}")
print(f"Price 3 is ${price3:.3f}")

#number after ':' to add that many spaces
print("\n---Spaces---")
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
#add zero to the front to use it as the space
print(f"Price 3 is ${price3:010}")

#justifying to the left with :<
print("\n---Left---")
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

#justifying to the right with :> (default)
print("\n---Right---")
print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")

#centering with :^
print("\n---Center---")
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")

#Showing if a number is positive with :+ (or just : ) -adds plus sign
#                                                      to positive numbers
print("\n---Positive or negative---")
print(f"Price 1 is ${price1:+10}")
print(f"Price 2 is ${price2:+10}")
print(f"Price 3 is ${price3:+10}")

#Separating a number if it is thousands with comma for easier readability
#use :,
print("\n---Comma---")
#added 3k to demonstrate
print(f"Price 1 is ${price1 +3000:+,.2f}") #you can use .number along with it to fix decimal
print(f"Price 2 is ${price2 -3000:+,.2f}") #you can also mix match with + to see if it is positive
print(f"Price 3 is ${price3 +3000:+,.2f}")