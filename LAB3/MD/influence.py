import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, current_node = heapq.heappop(pq)
        if dist > distances[current_node]:
            continue

        for neighbor, weight in graph.get(current_node, {}).items():
            old_dist = distances[neighbor]
            new_dist = dist + weight
            if new_dist < old_dist:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances

def calculate_ratings(graph):
    ratings = {}
    for node in graph:
        distances = dijkstra(graph, node)
        rating = 0
        # Distance D contributes (D - 1) points
        for target, dist in distances.items():
            if dist != float('infinity') and dist > 0:
                rating += (dist - 1)
        ratings[node] = rating
    return ratings
with open('matrix.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

header = lines[0].split("|")
names = [name.strip() for name in header if name.strip()]
graph = {name: {} for name in names}

for line in lines[1:]:
    parts = [p.strip() for p in line.split("|") if p.strip() != ""]
    if len(parts) == 0:
        continue

    person = parts[0]
    connections = parts[1:]
    if len(connections) != len(names):
        raise ValueError(f"The line for {person} does not have the correct number of connections.")

    if person not in graph:
        raise ValueError(f"Person '{person}' not found in the header names.")

    for idx, is_friend_str in enumerate(connections):
        if not is_friend_str.isdigit():
            raise ValueError(f"Non-digit value in connections for {person}: '{is_friend_str}'")

        is_friend = int(is_friend_str)
        if is_friend == 1:
            friend_name = names[idx]
            if friend_name not in graph:
                raise ValueError(f"Friend '{friend_name}' not found in the header names.")
            graph[person][friend_name] = 1
ratings = calculate_ratings(graph)

posting_rates = {}
with open('influence.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(":")
        person = parts[0].strip()
        rate = float(parts[1].strip())
        posting_rates[person] = rate

new_ratings = {}
for person, old_rating in ratings.items():
    if person in posting_rates:
        new_ratings[person] = old_rating * (0.5 * posting_rates[person])
    else:
        new_ratings[person] = 0
sorted_by_new_rating = sorted(new_ratings.items(), key=lambda x: x[1], reverse=True)
for person, nr in sorted_by_new_rating:
    print(f"{person}: {nr}")