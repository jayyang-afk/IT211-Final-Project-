#Yang_P1P2.py
#"breakfast" or "lunch" or "dinner"
meal_time = input("Breakfast, Lunch or Dinner?")

#breakfast meal options:
if meal_time == "Breakfast" or meal_time == "breakfast":
    mea1_options = input("pick a number, 1:pancake, 2:omelette, 3:smoothie:")
#1.) Pancakes with your choice of syrup: Maple, Berry or Chocolate
    if mea1_options == "1":
        pancake_choice = input("Your choice of syrup: Maple, berry or chocolate:")
#(Breakfast meal #1)answer a syrup is maple(no cap), or a cap(Maple),
#print it
        if pancake_choice == "maple" or pancake_choice == "Maple":
            print("Your order: pancake with maple syrup")
#(Breakfast meal #1)answer a syrup is berry(no cap), or a cap(Berry),
#print it
        elif pancake_choice == "berry" or pancake_choice == "Berry":
            print("Your order: pancake with berry syrup")
#(Breakfast meal #1)answer chocolate(no cap) or a cap(Chocolate),
#print it
        elif pancake_choice == "chocolate" or pancake_choice == "Chocolate":
            print("Your order: pancake with chocolate syrup")
#2.) Omelette with your choice of filling: Cheese Ham or Veggie
    elif mea1_options == "2":
        omelette_choice = input("Your choice of filling: Cheese, ham, veggie:")
#(Breakfast meal #2)answer a cap(Cheese), or no cap(cheese)
#print it
        if omelette_choice == "cheese" or omelette_choice == "Cheese":
            print("Your order: Omelette with cheese filling")
#(Breakfast meal #2)answer a no cap(ham) or cap(Ham)
#print it
        elif omelette_choice == "ham" or omelette_choice == "Ham":
            print("Your order: Omelette with ham filling")
#(Breakfast meal #2)Answer a cap(Ham) or no cap(ham)
#print it
        elif omeletee_choice == "veggie" or omelette_choice == "Veggie":
            print("Your order Omelette with veggie filling")
#3.) Smoothie with your choice of base: Yogurt, Almond milk or Juice
    elif mea1_options == "3":
        smoothie_choice = input("Your choice of base: Yogurt, almond milk, juice:")
#(Breakfast meal #3)if pressing "yogurt" or "Yogurt",
#print it
        if smoothie_choice == "yogurt" or smoothie_choice == "Yogurt":
            print("Your order: Smoothie with yogurt base")
#(Breakfast meal #3)if pressing "almond milk" or "Almond milk",
#print it
        elif smoothie_choice == "almond milk" or smoothie_choice == "Almond milk":
            print("Your order: Smoothie with almond milk base")
#(Breakfast meal #3)if pressing "juice" or Juice",
#print it
        elif smoothie_choice == "juice" or smoothie_choice == "Juice":
            print("Your order: Smoothie with juice base")
#Lunch Meal Options
elif meal_time == "Lunch" or meal_time == "lunch":
    mea2_options = input("Pick a number, 1: casear salad, 2: spicy chicken wrap, 3:butternut squash soup:")
#1.)Casear salad with your choice of dressing: Rach Casear or Vinaigrette
    if mea2_options == "1":
        casear_salad_choice = input("Your choice of dressing: Ranch, casear or vinaigrette")
#(Lunch meal #1)if "Ranch" or "ranch",
#print it
        if casear_salad_choice == "ranch" or casear_salad_choice == "Ranch":
            print("Your order: Casear salad with ranch dressing")
#(Lunch meal #1)if "Casear" or "casear",
#print it
        elif casear_salad_choice == "casear" or casear_salad_choice == "Casear":
            print("Your order: Casear salad with casear dressing")
#(Lunch meal #1)if "vinaigrette" or "Vinaigrette",
#print it
        elif casear_salad_choice == "vinaigrette" or casear_salad_choice == "Vinaigrette":
            print("Your order: Casear salad with vinaigrette dressing")
#2.)Spicy chicken wrap with your choice of sauce: Buffalo, Ranch, or BBQ
    elif mea2_options == "2":
        spicy_chicken_wrap_choice = input("Your choice of sauce: Buffalo, ranch or BBQ:")
#(Lunch meal #2)typing "buffalo" or "Buffalo"
#print it
        if spicy_chicken_wrap_choice == "buffalo" or spicy_chicken_wrap_choice == "Buffalo":
            print("Your order: Spicy chicken wrap with buffalo sauce")
#(Lunch meal #2)typing "ranch" or "Ranch"
#print it
        elif spicy_chicken_wrap_choice == "ranch" or spicy_chicken_wrap_choice == "Ranch":
            print("Your order: Spicy chicken wrap with ranch sauce")
#(Lunch meal #2)typing "bbq" or "BBQ",
#print it
        elif spicy_chicken_wrap_choice == "BBQ" or spicy_chicken_wrap_choice == "bbq":
            print("Your order: Spicy chicken wrap with BBQ sauce")
#3.)Butternut squash soup with your choice of topping: Croutons, Cheese, or Chives
    elif mea2_options == "3":
        butternut_squash_soup_choice = input("Your choice of topping: Croutons, cheese or chives:")
#(Lunch meal #3)if "croutons" or "Croutons",
#print it
        if butternut_squash_soup_choice == "croutons" or butternut_squash_soup_choice == "Croutons":
            print("Your order: Butter squash soup with croutons topping")
#(Lunch meal #3)if "cheese" or "Cheese",
#print it
        elif butternut_squash_soup_choice == "cheese" or butternut_squash_soup_choice == "Cheese":
            print("Your order: Butter squash soup with cheese topping")
#(Lunch meal #3)if "chives" or "Chives",
#print it
        elif butternut_squash_soup_choice == "chives" or butternut_squash_soup_choice == "Chives":
            print("Your order: Butter squash soup with chives topping")
#Dinner Meal Options
elif meal_time == "Dinner" or meal_time == "dinner":
    mea3_options = input("Pick a number, 1: baked salmon, 2: turkey burger, 3: mushroom risotto:")
#1.)Baked salmon with your choice of side: Rice, Quinoa, or Mashed potaoes
    if mea3_options == "1":
        baked_salmon_choice = input("Your choice of side: rice, quinoa or mashed potatoes:")
#(Dinner meal #1)Answer a side is "rice", or "Rice"
#print it
        if baked_salmon_choice == "rice" or baked_salmon_choice == "Rice":
            print("Your order: Baked salmon with rice side")
#(Dinner meal #1)Answer a side is "quinoa", or "Quinoa"
#print it
        elif baked_salmon_choice == "quinoa" or baked_salmon_choice == "Quinoa":
            print("Your order: Baked salmon with quinoa side")
#(Dinner meal #1)Answer a side is "mashed potatoes", or "Mashed potatoes"
#print it
        elif baked_salmon_choice == "mashed potatoes" or baked_salmon_choice == "Mashed potatoes":
            print("Your order: Baked salmon with mashed potatoes side")
#2.)Turkey burger with your choice of topping: Avocado, Bacon, or Mushrooms
    elif mea3_options == "2":
        turkey_burger_choice = input("Your choice of topping: Avocado, bacon or mushrooms:")
#(Dinner meal #2)Answer a topping is "avocado", or "Avocado"
#print it
        if turkey_burger_choice == "avocado" or turkey_burger_choice == "Avocado":
            print("Your order: Turkey burger with avocado topping")
#(Dinner meal #2)Answer a topping is bacon,
#print it
        elif turkey_burger_choice == "bacon" or turkey_burger_choice == "Bacon":
            print("Your order: Turkey burger with bacon topping")
#(Dinner meal #2)Answer a topping is mushroomm print it
        elif turkey_burger_choice == "mushroom" or turkey_burger_choice == "Mushroom":
            print("Your order: Turkey burger with mushroom topping")
#3.)Mushroom risotto with your choice of garnish: Parmesan, Parsley, or Truffle oil
    elif mea3_options == "3":
        mushroom_risotto_choice = input("Your choice of garnish: Parmesan, parsley or truffle oil:")
#(Dinner meal #3)if answer a garnish is "parmesan", or "Parmesan"
#print it.
        if mushroom_risotto_choice == "parmesan" or mushroom_risotto_choice == "Parmesan":
            print("Your order: Mushroom risotto with parmesan garnish")
#(Dinner meal #3)if answer a garnish is "parsley", or "Parsley"
#print it.
        elif mushroom_risotto_choice == "parsley" or mushroom_risotto_choice == "Parsley":
            print("Your order: Mushroom risotto with parsley garnish")
#(Dinner meal #3)if answer a garnish is "truffle oil", or "Truffle oil"
#print it. 
        elif mushroom_risotto_choice == "truffle oil" or mushroom_risotto_choice == "Truffle oil":
            print("Your order: Mushroom risotto with truffle oil garnish")    









