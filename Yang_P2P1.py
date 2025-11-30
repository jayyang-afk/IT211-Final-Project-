#Yang_P2P1.py
#Jay Yang
#Tuesday, October 7, 2025

#data_processing import from data_processing processing file
from data_processing import calculate_average, find_max, count_vowels
#average number = [5, 10, 15]
number = [5, 10, 15]
#max number = [3, 8, 2, 10]
numbers = [3, 8, 2, 10]
#Vowel count(a, e, i, o, u) = "Hello World"
text = "Hello World"

#print it("10.0") = [5, 10, 15] = 30 / 3 = 10.0
print("The average:", calculate_average(number))
#print it("10") = [3, 8 , 2, 10] = 10
print("The maximum value:", find_max(numbers))
#print it("3") = e, o, o = Hello World  
print("The number of vowels", count_vowels(text))



"""
numbers = input("Max numbers:")
number = input("Average numbers:")
text = input("Vowel texts:")

"""
