# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []                                 # define result list
    cache = {}                                  # define cache dictionary
    for path in files:                          # check all paths
        if path in cache:                       # if the path exists in cache
            result.append(path)                 # append the path to the cache dictionary
            break                               # end. path is already in cache
        pathSplit = path.split('/')             # split string at '/' to create list
        lastItem = pathSplit[len(pathSplit) - 1]# get last item in the list
        if lastItem in queries:                 # if the last item in the array matches what is in the queries
            result.append(path)                 # append the path to the resuls list (line 8)

    return result                               # return the result
 

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
