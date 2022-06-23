from moon_utils import random_sample
from django.shortcuts import render
import numpy as np
from moon_utils import *
import matplotlib.pyplot as plt
from geopy.distance import geodesic
import pandas as pd

def calc(request):
    ctx = {}
    if request.POST:
        country = request.POST['c']
        n = int(request.POST['s'])
        id = range(1, n+1)
        coords = random_sample(country=country, n=n)
        lat = [e[0] for e in coords]
        lon = [e[1] for e in coords]
        coords = zip(id, lat, lon)
        ctx['coords'] = coords

        #
        distence_matrix = np.zeros([n, n])
        for i in range(0, n):
            for j in range(n):
                dist = get_distance(stores[i], stores[j])
                distence_matrix[i][j] = dist

        S = Solution(distence_matrix, 0)
        # print("Shortest Path: " + str(S.tsp()) + "km")
        res = "Shortest Path: " + str(S.tsp()) + "km"
        M = S.array
        lists = list(range(len(S.X)))
        start = S.start_node
        store_order = []

        while len(lists) > 0:
            lists.pop(lists.index(start))
            m = S.transfer(lists)
            next_node = S.array[start][m]
            # print(start, "--->", next_node)
            res += f"{start} ---> {next_node}"
            store_order.append(stores[start])
            start = next_node

        ctx["res"] = res
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
        #

        return render(request, "app/delivery.html", ctx)