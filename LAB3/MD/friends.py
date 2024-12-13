def find_most_friends(filename):
    with open(filename, 'r') as f:
        lines = [line.strip().split() for line in f.readlines()]

    friendships = {person: set(friends) for person, *friends in (line[1:] for line in lines)}

    max_friends_person = max(friendships, key=lambda x: len(friendships[x]))

    return max_friends_person

print(find_most_friends('matrix.txt'))