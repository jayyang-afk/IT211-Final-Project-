#Yang_P1P3.py

#Pattern Question(Input)
n = int(input("The number of rows for each pattern:"))
#Symbol1 Question(Input)
j = input("Each containing a single character(symbol1):")
#Symbol2 Question(Input)
y = input("Each containing a single character(symbol2):")
#loop and n range(numbers only)
for m in range(0, n):
#Symbol1 calculator
    symbol1 = j * (n - m)
#Print a pattern using symbol1
    print(symbol1)
#Loop and n range(numbers only) 
for o in range(0, n):
#Symbol2 calculator
    symbol2 = y * (n - o)
#Print a pattern using symbol2 
    print(symbol2)
