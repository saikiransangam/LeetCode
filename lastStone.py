import heapq

def lastStone(stones):

    stones = [-s for s in stones]

    heapq.heapify(stones)

    while len(stones) > 1:

        first = heapq.heappop(stones)
        second = heapq.heappop(stones)

        if second > first:
            heapq.heappush(stones, first - second)

            print(stones)

    stones.append(0)

    return abs(stones[0])

print(lastStone([2,7,4,1,8,1]))