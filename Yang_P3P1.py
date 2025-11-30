#Yang_P3P1
#Jay Yang
#10/26/2025

#def categorize(age_list)
def categorize_ages(age_list):
#Result Dictionary{("Key"(adults/minors): Value(square braket)} 
    result = {"adults": [], "minors": []}
#Ages Input("Enter ages separated by spaces:").Split
ages = input("Enter ages separated by spaces: ").split()
#Ages Integer and Loopps
ages = [int(age) for age in ages]
#Age Group (adults loop) age more than 18,(minors loop) age less than 18
age_groups = {
    "adults": [age for age in ages if age >= 18],
    "minors": [age for age in ages if age < 18]
}
#Age Groups Print
print(age_groups)

