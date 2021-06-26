states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = dict(
    kone=set(['od', 'nv', 'ut']),
    ktwo=set(['wa', 'id', 'mt']),
    kthree=set(['or', 'nv', 'ca']),
    kfour=set(['nv', 'mt']),
    kfive=set(['ca', 'az'])
)

final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states  # area of coverage
        if (len(covered) > len(states_covered)):  # if coverage > current coverage
            best_station = station
            states_covered = covered
    states_needed = states_needed - states_covered
    final_stations.add(best_station)

print(final_stations)
