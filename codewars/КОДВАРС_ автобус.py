def number(bus_stops):
    k = 0
    for i in range(len(bus_stops)):
        k += bus_stops[i][0]
    j = 0
    for i in range(len(bus_stops)):
        j += bus_stops[i][1]
    if (k - j) >= 0:
        return k - j

print(number([[2, 1], [2, 4]]))