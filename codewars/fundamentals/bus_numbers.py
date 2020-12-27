def number(bus_stops):
    balance = list(map(sum, zip(*bus_stops)))
    return balance[0] - balance[1]
