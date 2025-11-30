#data processing
#Jay Yang
#Tuesday, October 7, 2025

#list max for numbers(input)
def find_max(numbers):
    x = max(numbers)
    return x


#average for number(input)
def calculate_average(number):
    x_average = (sum(number))/(len(number))
    return x_average


#vowels for text(input)
def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count







