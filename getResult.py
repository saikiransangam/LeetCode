def getResult(arrival, street):

# Write your code here

# The first car arrives on Main Street at time 0. The first car arrives on 1st Avenue at time 0. The second car arrives on Main Street at time
#1. The third car arrives on 1st Avenue at time 5.
    result = []
    time = 0
    main_street_queue = []
    first_avenue_queue = []

    while len(main_street_queue) > 0 or len(first_avenue_queue) > 0:

        if len(main_street_queue) == 0:
            car_to_add_to_result = first_avenue_queue.pop(0)
            time = car_to_add_to_result[1]
            result.append(time)
            continue
        if len(first_avenue_queue) == 0:
            car_to_add_to_result = main_street_queue.pop(0)
            time = car_to_add_to_result[1]
            result.append(time)
            continue

        if (time - main_street_queue[0][1]) > 1:
            car_to_add_to_result = first_avenue_queue.pop(0)
            time = car_to_add_to_result[1]      
            result.append(time)
            continue

        if (time - first_avenue_queue[0][1]) > 1:
            car_to_add_to_result = main_street_queue.pop(0)
            time = car_to_add_to_result[1]
            result.append(time)
            continue

        if main_street_queue[0][0] < first_avenue_queue[0][0]:
            car_to_add_to_result = main_street_queue.pop(0)
            time = car_to_add_to_result[1]
            result.append(time)
            continue
        else:
            car_to_add_to_result = first_avenue_queue.pop(0)
            time = car_to_add_to_result[1]
            result.append(time)
            continue

    return result


print(getResult([0, 0, 1, 5], [0, 1, 0, 1]))