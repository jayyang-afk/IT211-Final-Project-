#Yang_P2P3
#Jay Yang
#Thursday, October 8, 2025
#asking it("Enter a number of rows in the list:")
x = int(input("Enter a number of rows in the list:"))

#matrix = square braket
matrix = []
#range loop(x("Enter a number of rows in the list:")
for row in range(x):
#input_string = asking ("Enter a row)   
    input_string = input("Enter a row:")
#string_list split
    string_list = input_string.split()

#number_list = square braket
    number_list = []
#s = string_list
    for s in string_list:
#adding a float to number_list
        number_list.append(float(s))
#adding a number_list to matrix
    matrix.append(number_list)
#max_i = 0
max_i = 0
#max_j = 0
max_j = 0
#max_num float
max_num = float('-inf')
#i row = enumerate(matrix)
for i, row in enumerate(matrix):
#j num = enumerate(row)
    for j, num in enumerate(row):
#j, num is greater than max_num
        if num > max_num:
#max_num = num, j
            max_num = num
#max_i = i, row
            max_i = i
#max_j = j, num
            max_j = j    
#print it(The location of the larget element is at,
#max_i)(x), max_j(y)
print(f"The location of the largest element is at ({max_i},{max_j})")

