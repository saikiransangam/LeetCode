

def running_sum(self, nums):

    sum = 0

    res = []

    for i in range(len(nums)) :

        sum += nums[i]

        res.append(sum)

    return res



print(running_sum([1,2,3,4,5]))

        

