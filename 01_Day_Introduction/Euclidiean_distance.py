def euclidian_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return distance ** 0.5
print(euclidian_distance([1, 2], [3, 4]))

