#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    tickets = {x.source:x for x in tickets}     # create dict comprehension
    route = []                                  # define route as an array
    current = tickets["NONE"]                   # define current position - "NONE" from test

    while current.destination != "NONE":        # for all destinations  
        route.append(current.destination)       # append routes array with destinations
        current = tickets[current.destination]  # update current position

    route.append(current.destination)           # last destination gets appened to route
    return route                                # return route
