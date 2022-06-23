from moon_utils import *
import numpy as np
import matplotlib.pyplot as plt
from geopy.distance import geodesic
import pandas as pd


def get_distance(p1, p2):
    return geodesic(p1, p2).kilometers


class Solution:
    def __init__(self, X, start_node):
        self.X = X  # distance matrix
        self.start_node = start_node  # start node
        self.array = [[0] * (2 ** (len(self.X) - 1)) for i in range(len(self.X))]

    def transfer(self, sets):
        su = 0
        for s in sets:
            su = su + 2 ** (s - 1)
        return su

    def tsp(self):
        s = self.start_node
        num = len(self.X)
        cities = list(range(num))
        # past_sets = [s]
        cities.pop(cities.index(s))
        node = s
        return self.solve(node, cities)

    def solve(self, node, future_sets):
        # end condition
        if len(future_sets) == 0:
            return self.X[node][self.start_node]
        d = 10e10
        distance = []
        for i in range(len(future_sets)):
            s_i = future_sets[i]
            copy = future_sets[:]
            copy.pop(i)
            distance.append(self.X[node][s_i] + self.solve(s_i, copy))
        d = min(distance)
        next_one = future_sets[distance.index(d)]
        c = self.transfer(future_sets)
        self.array[node][c] = next_one
        return d


if __name__ == '__main__':

    country = 'US'
    csv_path = 'moonbucks.csv'
    n = 6
    stores = random_sample('US', csv_path, n)

    distence_matrix = np.zeros([n, n])
    for i in range(0, n):
        for j in range(n):
            dist = get_distance(stores[i], stores[j])
            distence_matrix[i][j] = dist

    S = Solution(distence_matrix, 0)
    print("Shortest Path: " + str(S.tsp()) + "km")
    M = S.array
    lists = list(range(len(S.X)))
    start = S.start_node
    store_order = []
    while len(lists) > 0:
        lists.pop(lists.index(start))
        m = S.transfer(lists)
        next_node = S.array[start][m]
        print(start, "--->", next_node)
        store_order.append(stores[start])
        start = next_node
    # plot
    x1 = []
    y1 = []
    for store in store_order:
        x1.append(store[0])
        y1.append(store[1])

    x2 = []
    y2 = []
    x2.append(store_order[-1][0])
    x2.append(store_order[0][0])
    y2.append(store_order[-1][1])
    y2.append(store_order[0][1])

    plt.plot(x1, y1, label='path', linewidth=2, marker='o')
    plt.plot(x2, y2, label='path', linewidth=2, color='g', marker='o')
    plt.xlabel('latitude')
    plt.ylabel('longitude')
    plt.title('TSP path')
    plt.legend()
    plt.savefig("path.png")
    plt.show()
