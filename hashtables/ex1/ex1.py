def get_indices_of_item_weights(weights, length, limit):
    """                            
    YOUR CODE HERE
    """
    # Your code here
    cache = {}                              # create cache dictionary for faster look ups
    for i in range(length):                 # loop through all items
        number = weights[i]                 # number = weight of the item 
        weightNeeded = limit - number       # find weight needed for each item
        if weightNeeded not in cache:       # add weight needed to cache dictionary if it doesn't exist
            cache[number] = i               # assign loop iteration number to equal cache index value
            print(cache)                    # cached kv pairs sent to terminal
            continue                        # continue
        weightNeeded = cache[weightNeeded]  # weight needed is given the cached value
        if i < weightNeeded:                # if index is less than cached index
            return (weightNeeded, i)        # return index
        else:                               # else
            return (i, weightNeeded)        # return index
    return None                             # return None if if-else statement did not return a value
