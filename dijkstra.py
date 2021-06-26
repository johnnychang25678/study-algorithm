# graph
infinity = float('inf')
graph = dict(
    start=dict(a=2, b=5),
    a=dict(b=8, c=7),
    b=dict(d=4, c=2),
    c=dict(finish=1),
    d=dict(c=6, finish=3),
    finish=dict()
)
# costs
costs = dict(
    a=2,
    b=5,
    c=infinity,
    d=infinity,
    finish=infinity
)

# parent
parents = dict(
    a='start',
    b='start',
    c=None,
    d=None,
    finish=None
)

processed = []


def dijkstra(graph, costs, parents):
    def find_lowest_cost_node(costs, processed):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            if costs[node] < lowest_cost and node not in processed:
                lowest_cost = costs[node]
                lowest_cost_node = node
        return lowest_cost_node  # return None if costs[node] = infinity

    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost_from_start_to_node = costs[node]  # cost from start to the node
        neighbors = graph[node]  # a dict of the node's neighbor
        for n in neighbors:
            new_cost = cost_from_start_to_node + neighbors[n]
            # compare if i go start -> node -> neighbor vs. current start -> neighbor
            if new_cost < costs[n]:
                costs[n] = new_cost  # update the costs table
                # update n's parent to current node we are checking
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    print(parents)  # start -> b -> c -> fin
    return costs['finish']  # lowest cost from start to finish


res = dijkstra(graph, costs, parents)
print(res)
