from math import sqrt, inf
from operator import itemgetter, attrgetter


P = [[6, 10],
     [7, 8],
     [1, 4],
     [1, 17],
     [9, 7],
     [19, 6],
     [4, 18],
     [10, 16],
     [14, 2],
     [12, 10],
     [7, 1],
     [11, 7],
     [2, 11],
     [14, 14],
     [3, 2],
     [1, 8],
     [10, 17],
     [18, 2],
     [5, 15],
     [13, 7]]
# P = [(2, 4), (9, 3), (-3, -8), (-2, -7), (-1, 7), (8, 5), (6, 0), (3, -5)]

Px = sorted(P, key=itemgetter(0))
Py = sorted(P, key=itemgetter(1))

# print(Px)
# print(Py)


def brute_force_closest_pair(P):
    min_distance = euclidean_distance(P[0], P[1])
    min_points = [P[0], P[1]]
    for i, point1 in enumerate(P[: -1]):
        for j, point2 in enumerate(P[i + 1:], ):
            new_min_dist = euclidean_distance(point1, point2)
            if new_min_dist < min_distance:
                min_distance = new_min_dist
                min_points = [point1, point2]

    return min_points[0], min_points[1], min_distance


def closest_split_pair(Px, Py, d, p3, q3):
    x_bar = Px[len(Px) // 2][0]
    sy = []
    for index, item in enumerate(Py):
        if abs(item[0] - x_bar) < d:
            sy.append(item)

    best = d
    for i in range(len(sy) - 1):
        # for j in range(1, min(i + 7, (len(sy) - i))):
        #     dist = euclidean_distance(sy[i], sy[i+j])
        #     if dist < best:
        #         best, p3, q3 = dist, sy[i], sy[i+j]
        k = i + 1
        while k < len(sy) and sy[k][1] - sy[i][1] < d:
            dist = euclidean_distance(sy[i], sy[k])
            if dist < best:
                best, p3, q3 = dist, sy[i], sy[k]
            k += 1

    return p3, q3, best


def closest_pair(px, py):
    if len(px) == 1:
        return None, None, inf

    if len(px) == 2:
        return px[0], px[1], euclidean_distance(px[0], px[1])

    mid = len(px) // 2
    x_l = px[: mid]
    x_r = px[mid:]

    y_l, y_r = [], []
    x_divider = x_l[-1][0]

    for p in py:
        if p[0] <= x_divider:
            y_l.append(p)
        else:
            y_r.append(p)

    p1, q1, dist_l = closest_pair(x_l, y_l)
    p2, q2, dist_r = closest_pair(x_r, y_r)

    p_min, q_min, d = min((p1, q1, dist_l), (p2, q2, dist_r), key=itemgetter(2))
    p3, q3, dist3 = closest_split_pair(px, py, d, p_min, q_min)
    return min((p1, q1, dist_l), (p2, q2, dist_r), (p3, q3, dist3), key=itemgetter(2))


def euclidean_distance(p1, p2):
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]

    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


# brute_force_closest_pair(P)
# print(brute_force_closest_pair(P))

print(closest_pair(Px, Py))
