#Yang_P3P2
#Jay Yang
#10/26/2025

#Class Recipe
class Recipe:
    
#Category is "Baking Recipes"
    category = "Baking Recipes"
    
#Define instance self
    def __init__(self):
#Recipe name
        self.name = ''
#Recipe ingredients list(square bracket)
        self.ingredients = []
#Recipe prepation time starts at 0
        self.prep_time = 0
#Recipe servings starts at 0
        self.servings = 0
        
#Define print_recipe self
    def print_recipe(self):
#Recipe Name Print("Recipe Name: name 1 and 2")     
        print(f"\nRecipe Name: {self.name}")
#Recipe Catoegory Print("Baking Recipes")      
        print(f"Category: {Recipe.category}")
#Ingredients Print("Ingredients: Ingredients 1 and 2")        
        print(f"Ingredients: {', '.join(self.ingredients)}")
#Preparation Time Print("Preparation Time: Preparation 1 and 2")  
        print(f"Preparation Time: {self.prep_time} minutes")
#Servings Print("Servings: servings 1 and 2")       
        print(f"Servings: {self.servings}")


#First Recipe's Input
#(name, ingrendients, preparation time, serving) 

#First recipe name input
name1 = input("Enter the name of the first recipe for:")
#First recipe ingredients input
ingredients1 = input("Enter ingredients for the first recipe (separated by commas):")
#First recipe preparation time input
prep_time1 = int(input("Enter preparation time (in minutes) for the first recipe:"))
#First recipe serving input
servings1 = int(input("Enter number of servings for the first recipe:"))

#Create the first Recipe object
#recipe1 = Class recipe(category = "Baking Recipes")
recipe1 = Recipe()
#first recipe(self name) to name1 input
recipe1.name = name1
#first recipe(self ingrendients) to ingredients1 input
recipe1.ingredients = [ingredient.strip() for ingredient in ingredients1.split(',')]
#first recipe(self prep_time) to prep_time1 input
recipe1.prep_time = prep_time1
#first recipe(self servings) to servings1 input
recipe1.servings = servings1


#Second Recipe's Input
#(name, ingrendients, preparation time, serving) 

#Second recipe name input
name2 = input("Enter the name of the second recipe for:")
#Second recipe ingredients input
ingredients2 = input("Enter ingredients for the second recipe (separated by commas):")
#Second recipe preparation time input
prep_time2 = int(input("Enter preparation time (in minutes) for the second recipe:"))
#Second recipe serving input
servings2 = int(input("Enter number of servings for the second recipe:"))

#Create the second Recipe object
#Recipe2 = Class recipe(category = "Baking Recipes")
recipe2 = Recipe()
#Second recipe(self name) to name2 input
recipe2.name = name2
#Second recipe(self ingrendients) to ingredients2 input
recipe2.ingredients = [ingredient.strip() for ingredient in ingredients2.split(',')]
#Second recipe(self prep_time) to prep_time2 input
recipe2.prep_time = prep_time2
#Second recipe(self servings) to servings2 input
recipe2.servings = servings2

#recipe1 input to def print_recipe, then print it
#(name, ingrendients, preparation time, serving)
recipe1.print_recipe()


#recipe2 input to def print recipe, then print it 
#(name, ingrendients, preparation time, serving) 
recipe2.print_recipe()

