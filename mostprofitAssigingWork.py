def mostProfit(difficulty: list[int], profit: list[int], workers: list[int]) -> int:
    # Combine difficulty and profit into tuples and sort them by difficulty
    jobs = sorted(zip(difficulty, profit), key=lambda x: x[0])

    maxprof = 0
    current_max_profit = 0
    j = 0

    for i in sorted(workers):
        while j < len(jobs) and i >= jobs[j][0]:
            current_max_profit = max(current_max_profit, jobs[j][1])
            j += 1
        maxprof += current_max_profit

    return maxprof


difficulty = [68, 35, 52, 47, 86]
profit = [67, 17, 1, 81, 3]
worker = [92, 10, 85, 84, 82]

print(mostProfit(difficulty, profit, worker))
