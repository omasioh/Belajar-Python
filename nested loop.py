# nested loop = a loop within an another loop (outer, inner)
#               outer loop will execute one time for each iteration of the inner loop
#               inner loop will execute one time for each iteration of the outer loop

rows = int(input("Input number of rows: "))
Columns = int(input("Input number of columns:"))
Symbols = input("Input a symbol to use:")


for x in range(rows):
    for y in range(Columns): 
        print(Symbols, end="")
    print()