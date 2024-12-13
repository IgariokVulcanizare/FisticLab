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
chosen_interests = {"Football", "Internet", "Politics", "Art", "Cats"}
people_interests = {}
with open('people_interests.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(":")
        person = parts[0].strip()
        if len(parts) > 1:
            interests_line = parts[1].strip()
            interests = set(interests_line.split())
        else:
            interests = set()
        people_interests[person] = interests
final_scores = {}
for person in people_interests:
    overlap_count = len(people_interests[person].intersection(chosen_interests))
    person_rating = ratings.get(person, 0)
    final_score = person_rating * (0.2 * overlap_count)
    final_scores[person] = final_score
sorted_people = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
print("Top 5 people to contact:")
for i, (person, score) in enumerate(sorted_people[:5], start=1):
    print(f"{i}. {person} - Final Score: {score}")
