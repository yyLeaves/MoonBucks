from matplotlib import pyplot as plt


def shellSort(A, n):
    # set the initial gap to floor of n/2
    gap = n // 2

    # Rearrange the array elements at n/2, n/4, ..., 1 intervals
    while gap > 0:

        for i in range(gap, n):
            temp = A[i]
            j = i

            while j >= gap and A[j - gap] < temp:
                A[j] = A[j - gap]

                j -= gap

            A[j] = temp
        gap //= 2


def getMax(array_A):
    max = array_A[0]
    for i in range(len(array_A)):
        if array_A[i] > max:
            max = array_A[i]

    return max


def plotPie(countries, probability):
    plt.pie(probability, labels=countries, explode=[0, 0.2, 0, 0, 0], shadow=True,
            autopct=lambda p: '{:.2f}%'.format(p),
            startangle=180)
    plt.title("Probability of Selecting Country to Expand Business")
    plt.show()


def get_prob(countries, scores, costs, n):
    total_score = 0
    total_cost = 0
    probability = []
    for score in scores:
        total_score += score

    for cost in costs:
        total_cost += cost

    print("Calculated Probability")
    for i in range(n):
        p = scores[i] / total_score * (1 - (costs[i]) / total_cost)
        probability.append(p)
        print(f"The probability for country {countries[i]} is {p:.5f}")

    arr = probability.copy()
    shellSort(arr, n)

    sorted_sequence_of_country = []
    for x in range(n):
        for y in range(n):
            if arr[x] == probability[y]:
                sorted_sequence_of_country.append(y)

    print("Sorted Probability")
    for i in range(n):
        print(f"Top {i + 1} --> {arr[i]}")

    print("Countries Ranking")
    for i in range(n):
        print(f"{i + 1} -> {countries[sorted_sequence_of_country[i]]}")

    plotPie(countries, probability)


if __name__ == '__init__':
    countries = ["US", "CA", "JP", "CN", "UK"]
    scores = [1.43, 0.87, 4.72, 0.19, 2.57]
    costs = [9700, 6777, 1721, 4292, 715]
    get_prob(countries, scores, costs, 5)
