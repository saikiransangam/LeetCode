def closestNumbers(numbers):

    numbers.sort()

    diff = float("inf")

    for i in range(len(numbers) - 1):

        diff = min(diff, numbers[i+1] - numbers[i])

    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] == diff:
            print(str(numbers[i]) + " " + str(numbers[i]))


print(closestNumbers([4,2,1,3]))

