"""
Greedy algorithm for the Knapsack problem
Only optimal for fractional Knapsack !
"""

class FractionalKnapsack(object):
    def __init__(self):

    def knapsackGreProc(self, W, V, M, n):
        packs = []
        for i in range(n):
            packs.append(KnapsackPackage(W[i], V[i]))

        packs.sort(reverse = True)

        remain = M
        result = 0

        i = 0
        stopProc = False

        while (stopProc != True):
            if (packs[i].weight <= remain):
                remain -= packs[i].weight;
                result += packs[i].value;

                print("Pack ", i, " - Weight ", packs[i].weight, " - Value ", packs[i].value)

            if (packs[i].weight > remain):
                i += 1

            if (i == n):
                stopProc = True

        print("Max Value:\t", result)
