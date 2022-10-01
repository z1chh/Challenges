def greedy(num_items, item_list, order):
    l = []
    last_added = 0
    while sum(l) != order:
        added = False
        for i in range(last_added, len(item_list)):
            item = item_list[i]
            if sum(l) + item <= order:
                added = True
                last_added = i + 1
                l.append(item)
                break
        if added:
            last_added = 0
        else:
            l.pop()
    print(l)
    return l


def reverse_greedy(num_items, item_list, order):
    return greedy(num_items, item_list[::-1], order)


# Get input
num_items = int(input())
item_list = list(map(int, input().split()))
num_orders = int(input())
order_list = list(map(int, input().split()))

# Dynamic programming for each order
for order in order_list:
    # If no order, no item ordered
    if order == 0:
        print(0)
        continue
    
    # Reset the arrays
    min_number_items = [order + 1] * (order + 1)
    min_number_items[0] = 0
    last_item_used = [order + 1] * (order + 1)
    last_item_used[0] = 0
    
    for i in range(1, order + 1):
        minimum = [min_number_items[i]]
        items = [-1]
        for item in item_list:
            if item > i:
                continue
            else:
                minimum.append(min_number_items[i - item] + 1)
                items.append(item)
        
        # Get minimum
        index = 0
        for j in range(1, len(minimum)):
            if minimum[j] < minimum[index]:
                index = j
        min_number_items[i] = minimum[index]
        last_item_used[i] = items[index]
    
    # Check if a solution was found
    if min_number_items[order] == order + 1:
        print("Impossible")
    else:
        # Get the list of items ordered
        last_item = last_item_used[order]
        items = [last_item]
        index = order
        while index != 0:
            index -= last_item
            if index != 0:
                last_item = last_item_used[index]
                items.append(last_item)
        
        # UNSAFE WAY TO CHECK FOR AMBIGUOUS
        l1 = greedy(num_items, item_list, order)
        l2 = reverse_greedy(num_items, item_list, order)
        l1.sort()
        l2.sort()
        items.sort()
        if not l1 == l2 == items:
            print("Ambiguous")
        else:
            # Get the indexes of these items, sorted
            indexes = []
            for item in items:
                for i, it in enumerate(item_list):
                    if item == it:
                        indexes.append(i + 1)
            indexes.sort()
            indexes = list(map(str, indexes))
            print(" ".join(indexes))
        
        # Some debugging shii
        #print("minimum", minimum)
        #print("dp arr", min_number_items)
        #print("items used arr", last_item_used)