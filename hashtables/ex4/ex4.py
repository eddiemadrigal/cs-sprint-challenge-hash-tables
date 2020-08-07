from collections import Counter
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    mydict = Counter()      # my dictionary defined by Counter()
    for i in a:             # loop through each number element in the passed in list
        mydict[i] += 1      # for each element found, increment index

    result = [i for i in mydict.keys() if i > 0 and mydict[-i] > 0] # result = mydict keys if i > 0 and there is a negative equivalent

    return result   # return values found that are positive and have corresponding negative values


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
