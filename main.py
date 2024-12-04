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
    n = int(input("(n): ")) #nr of cities
    num_flights = int(input("length of fligths: ")) #nr of flights
    flights = []
    for _ in range(num_flights):
        flight = list(map(int, input("flights separated by space: ").split()))
        flights.append(flight)
    start = int(input("(src): "))
    destination = int(input("(dst): "))
    k = int(input("(k): "))
    g = Graph(n)
    for from_city, to_city, price in flights:
        g.graph[from_city].append((to_city, price))
    result = g.dijkstra(start, destination, k)
    print(result)
find_cheapest_price()
