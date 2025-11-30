#Yang_P1P1.py

#Bring a code(math) to P1P3.
import math
#Side Length question("Enter the the side of an octagon:")
side_length = float(input("Enter the side of an octagon:"))
#Permeter octagon calculator
permeter_octagon = 8 * side_length
#Area octagon calculator
area_octagon = 2 * (1 + math.sqrt(2)) * (2 ** side_length)
#Print permeter octagon(3 rounds). 
print("The perimeter of the octagon is", round(permeter_octagon,3), "units")
#Print area_octagon(3 rounds)
print("The area of the octagon is", round(area_octagon,3), "units square")

