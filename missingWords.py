def missingWords(s,t):

    parts = s.split()
    next_parts = t.split()

    missing = []

    i = 0
    j = 0

    for i in range(len(parts)):
        if j < len(next_parts) and parts[i] == next_parts[j]:

            j += 1

        else:
            missing.append(parts[i])

    return missing

    
print(missingWords("I am using HackerRank to improve programming", "am HackerRank to improve"))



'''

test case: 

Input:
s = "I am using HackerRank to improve programming"
t = "am HackerRank to improve"


output:

I
using
programming
'''