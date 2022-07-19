def find_sum(lst, k):
    lst.sort()
    ind1 = 0
    ind2 = 0
    for i in range(len(lst)):

        for j in range(len(lst)):

            if(lst[i] + lst[j] == k and i is not j):

                return[lst[i], lst[j]]



print(find_sum([1,2,3,4], 4))


