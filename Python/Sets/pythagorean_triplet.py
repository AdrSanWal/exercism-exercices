def triplets_with_sum(number):
    results = list()
    a_limit = number // 3
    for a in range(1, a_limit):
        b_limit = (number - a + 1) // 2
        for b in range(a + 1, b_limit):
            c = number - a - b
            if a ** 2 + b ** 2 == c ** 2:
                results.append([a, b, c])
                break
    return results

print(triplets_with_sum(30000))

# [
#     [1200, 14375, 14425],
#     [1875, 14000, 14125],
#     [5000, 12000, 13000],
#     [6000, 11250, 12750],
#     [7500, 10000, 12500],
# ]
