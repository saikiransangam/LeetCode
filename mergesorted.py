

def mergesorted(lst1, lst2):

    ind1 = 0 
    ind2 = 0   #initialize two indices

    while (ind1 < len(lst1) and ind2 < len(lst2)):

        if (lst1[ind1] > lst2[ind2]):

            lst1.insert(ind1, lst2[ind2])

            ind1 += 1
            ind2 += 1

        else:
            ind1 += 1

    if ind2 < len(lst2):
        lst1.extend(lst2[ind2:])

    return lst1



print(mergesorted([1,2,4],[-2,-1,0,3]))

