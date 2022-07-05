from math import sqrt
t = int(input())
for i in range(t):
    n = int(input())
    coords = list(map(int, input().split()))
    areas = set()
    for x in coords:
        for x_2 in coords:
            if x == x_2:
                continue
            else:
                side_1 = sqrt((x - x_2) ** 2)
                side_2 = sqrt((x) ** 2 + (-1) ** 2)
                side_3 = sqrt((x_2) ** 2 + (-1) ** 2)
                s = 0.5 * (side_1 + side_2 + side_3)
                area = round(sqrt(s * ((s - side_1) * (s - side_2) * (s - side_3))), 2)
                areas.add(area)
    print(len(areas))