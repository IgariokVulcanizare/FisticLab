def sort_people_by_friends(filename):
    with open(filename, 'r') as f:
        lines = [line.strip().split() for line in f.readlines()]

    sorted_people = sorted([(name, len(set(friends))) for name, *friends in (line[1:] for line in lines)], key=lambda x: x[1], reverse=True)

    return [f"{person} - {num_friends}" for person, num_friends in sorted_people]

print(sort_people_by_friends('matrix.txt'))