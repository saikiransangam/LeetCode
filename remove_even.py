def remove_event(lst):

    odds = []

    for val in lst:

        if val % 2 != 0:

            odds.append(val)
        
    return odds









print(remove_event([1,2,3,4,5,6,7]))