nc = int(input())
while nc != 0:
    # Reset ingredients dict
    ingredients = {}

    # Get orders
    for i in range(nc):
        # Get customer and the food they ordered
        s = input()
        l = s.split()
        customer = l[0]
        l = l[1:]

        # Put ingredients in dict
        for ingredient in l:
            if ingredient in ingredients:
                ingredients[ingredient].append(customer)
            else:
                ingredients[ingredient] = [customer]

    # Print out ingredients and who ordered them
    for ingredient in sorted(ingredients):
        print(ingredient, " ".join(sorted(ingredients[ingredient])))

    # Print a blank line after the report for each day
    print()

    # Check for next day
    nc = int(input())
