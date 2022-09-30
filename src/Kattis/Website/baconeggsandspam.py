nc = int(input())
while nc != 0:
    # Reset vars
    customers = []
    ingredients = {}

    # Get customers
    for i in range(nc):
        customers.append(input())

    for s in customers:
        # Get customer and the food they ordered
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
