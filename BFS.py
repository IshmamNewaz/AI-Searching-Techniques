from collections import deque
def graphReader():
    filename = "graph.txt"
    graph_data = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split() 
            if len(parts) == 2:
                node1, node2 = parts
                graph_data.append((node1, node2))
    graph = {}  

    for node1, node2 in graph_data:
        if node1 in graph:
            graph[node1].append(node2)
        else:
            graph[node1] = [node2]
        if node2 in graph:
            graph[node2].append(node1)
        else:
            graph[node2] = [node1]
    return graph
graph = graphReader()



def bfs(graph, start, goal):
    visited = set()
    queue = deque()
    queue.append(start)
    
    paths = {start: [start]}  

    while queue:
        current = queue.popleft()

        if current == goal:
            return paths[current]  

        if current not in visited:
            visited.add(current)
            neighbors = graph[current]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    paths[neighbor] = paths[current] + [neighbor]  
    return None  

graph = graphReader()

start_node = 'A'
goal_node = 'F'

path = bfs(graph, start_node, goal_node)

if path:
    print("Path from {} to {}:".format(start_node, goal_node))
    print(" -> ".join(path))
else:
    print("No path found from {} to {}.".format(start_node, goal_node))
