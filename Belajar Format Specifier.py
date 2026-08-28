# Format speciefiers = {value:flags} format a value based on waht flags are inserted

# .(number)f =round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zoro pad that many spaces
# :< = left justify
# :> = right justify 
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position 
# :  = insert a space before positive numbers 
# :, - comma separator

price1 = 3.14159
price2 = -978.789
price3 = 123.456

print(f"Price 1 is {price1 :,.2f}")
print(f"Price 2 is {price2 :+,.10f}")
print(f"Price 3 is {price3 :+,.10f}")