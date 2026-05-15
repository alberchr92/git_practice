requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'onions', 'pineapple', 'green peppers']
for requested_topping in requested_toppings:
    if 'mushrooms' in requested_toppings:
        print("Sorry, we are out of anchovies right now.")
    else:
        print(f"Adding {requested_topping}.")

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

requested_toppings = []
if requested_topping:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.") 
    print("\nFinished making your pizza!") 
else:
    print("Are you sure you want a plain pizza?")