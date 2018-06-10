def maxProfitAssignment(self, difficulty, profit, workers):
    n = len(difficulty)
    i = result = best = 0

    jobs = zip(difficulty, profit)
    jobs.sort()
    workers.sort()

    for skill in workers:
        while i < n and skill >= jobs[i][0]:
            best = max(best, jobs[i][1])
            i += 1

        result += best

    return result