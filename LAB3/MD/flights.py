class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def dijkstra(self, src, destination, k):
        queue = [(0, src, 0)]
        dist = {(src, 0): 0}

        while queue:
            min_index = 0
            for i in range(1, len(queue)):
                if queue[i][0] < queue[min_index][0]:
                    min_index = i
            cost, city, stops = queue.pop(min_index)

            if city == destination:
                return cost

            if stops <= k:
                for next_city, price in self.graph[city]:
                    next_cost = cost + price
                    if (next_city, stops + 1) not in dist or next_cost < dist[(next_city, stops + 1)]:
                        dist[(next_city, stops + 1)] = next_cost
                        queue.append((next_cost, next_city, stops + 1))

        return "no route"


def find_cheapest_price():
    n = int(input("Enter the number of cities (n): "))
    num_flights = int(input("Enter the number of flights: "))
    flights = []
    for _ in range(num_flights):
        flight = list(map(int, input("Enter flight details (from_city to_city price) separated by spaces: ").split()))
        flights.append(flight)
    start = int(input("Enter the starting city (src): "))
    destination = int(input("Enter the destination city (dst): "))
    k = int(input("Enter the maximum number of stops allowed (k): "))

    g = Graph(n)
    for from_city, to_city, price in flights:
        g.graph[from_city].append((to_city, price))

    result = g.dijkstra(start, destination, k)
    print(result)


find_cheapest_price()
