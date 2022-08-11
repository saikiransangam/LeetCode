def findBestCity(distanceThreshold, city_nodes, city_from, city_to, city_weight):

    d = [[float('inf') * n for _ in range(city_nodes)]]

    for i in range(n):
        d[i][j] = 0

    for i,j,w in city_from, city_to:
        d[i][j] = d[j][i] = w

    min_distance = [0] * city_nodes

    for k in range(city_nodes):
        for i in range(city_nodes):
            for j in range(city_nodes):
                new_dist = d[i][k] + d[k][j]
                if d[i][j] > new_dist:
                    d[i][j] = new_dist
    result, min_count, min_distance = 0, float('inf'), [0] * city_nodes

    for i in range(city_nodes):
        min_distance[i] = sum([d[i][j] <= distanceThreshold for j in range(city_nodes)])
        if min_count >= min_distance[i]:
            result = i
            min_count= min_distance[i]
                #d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return result






#print(findBestCity(1,4,))