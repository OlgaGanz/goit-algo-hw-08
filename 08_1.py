import heapq


def min_cost_to_connect_cables(cables):
    if not cables:
        return 0

    heapq.heapify(cables)
    # print("Відсортовані кабелі:",cables)
    total_lenght = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_lenght += cost

        heapq.heappush(cables, cost)
        # print("After push: ", cables)
    return total_lenght


if __name__ == '__main__':
    cables = [1, 1, 9, 2, 1, 2]
    print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(cables))
    