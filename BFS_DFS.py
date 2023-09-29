from collections import deque

visited = list()
queue = deque([])
stack = list()


def BFS(start):
    visited.clear()
    global queue
    queue.append(start)
    visited.append(start)

    while queue:
        queue.popleft()
        for element in graph[start]:
            if element not in visited:
                visited.append(element)
                queue.append(element)

        if queue:
            start = queue[0]
    return visited


def DFS(start):
    visited.clear()
    global stack
    stack.append(start)
    visited.append(start)

    while stack:

        for element in graph[start]:
            if element not in visited:
                visited.append(element)
                stack.append(element)
                break

            elif stack:
                stack.pop()

        if stack:
            start = stack[-1]
    return visited


graph = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'D', 'F'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E', 'F'],
    'E': ['B', 'F', 'G'],
    'F': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'G': ['C', 'E', 'F']
}
visitedNode = BFS('A')
print(f'BFS Output: {visitedNode}')

visitedNode = DFS('A')
print(f'DFS Output: {visitedNode}')
