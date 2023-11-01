def graphReader():
    # Step 1: Open and read the file
    filename = "graph.txt"
    graph_data = []

    with open(filename, "r") as file:
        for line in file:
            # Step 2: Parse the file to extract the graph data
            parts = line.strip().split()  # Split the line into parts
            if len(parts) == 2:
                node1, node2 = parts
                graph_data.append((node1, node2))
    
    # Step 3: Represent the graph in your preferred data structure
    graph = {}  # You can represent the graph as an adjacency list (dictionary)

    for node1, node2 in graph_data:
        if node1 in graph:
            graph[node1].append(node2)
        else:
            graph[node1] = [node2]

        # Optionally, you may want to add the reverse edge as well, assuming it's an undirected graph.
        if node2 in graph:
            graph[node2].append(node1)
        else:
            graph[node2] = [node1]
    return graph
    # Display the graph
graph = graphReader()
print(graph)