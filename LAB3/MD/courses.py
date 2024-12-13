def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visited = [0] * numCourses
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)

    def dfs(i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for neighbor in graph[i]:
            if not dfs(neighbor):
                return False
        visited[i] = 1
        return True
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True

numCourses = int(input("Enter the number of courses: "))
prerequisites_count = int(input("Enter the number of prerequisites: "))
prerequisites = []

for _ in range(prerequisites_count):
    course, prerequisite = map(int, input("Enter a course and its prerequisite (separated by space): ").split())
    prerequisites.append((course, prerequisite))
if canFinish(numCourses, prerequisites):
    print("True")
else:
    print("False")
