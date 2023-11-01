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




def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if start == goal:
        path.append(start)
        return path 

    if start not in visited:
        visited.add(start)
        path.append(start)

        for neighbor in graph[start]:
            if neighbor not in visited:
                result = dfs(graph, neighbor, goal, visited, path)
                if result:
                    return result

        x =path.pop()  
        print (x)

    return None 


graph = graphReader()

start_node = 'A'
goal_node = 'F'

path = dfs(graph, start_node, goal_node)

if path:
    print("Path from {} to {}:".format(start_node, goal_node))
    print(" -> ".join(path))
else:
    print("No path found from {} to {}.".format(start_node, goal_node))