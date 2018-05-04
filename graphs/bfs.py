from collections import deque


def bfs(graph, start_vertex):
    # Add start vertex to shortest path list
    # shortest_path = [start_vertex]

    # comp_list = [start_vertex]
    # Set start vertex to explored
    graph[start_vertex][1] = 1

    # Set start vertex distance to 1
    # graph[start_vertex][2] = 1

    # Add start vertex to queue
    bfs_queue = deque([start_vertex])
    while len(bfs_queue) > 0:
        v = bfs_queue.popleft()
        # v_dist = graph[v][2]
        for w in graph[v][0]:
            # if unexplored
            if graph[w][1] == 0:
                graph[w][1] = 1
                # comp_list.append(w)
                # graph[w][2] = v_dist + 1
                bfs_queue.append(w)

    return graph


input_graph = {int(line.rstrip().split()[0]): [[int(i) for i in line.rstrip().split()[1:]], 0, 0] for line in
               open("../test_files/graphs/input_random_10_25.txt")}

g = {1: [[2, 3], 0, 0], 2: [[1, 4], 0, 0], 3: [[1, 4, 5], 0, 0], 4: [[2, 3, 5, 6], 0, 0], 5: [[3, 4, 6], 0, 0],
     6: [[4, 5], 0, 0]}

gra = {1: [[3, 5], 0], 3: [[1, 5], 0], 7: [[2], 0], 9: [[5], 0], 5: [[1, 3, 9], 0], 2: [[4,7], 0], 4: [[2], 0],
       6: [[8, 10], 0], 8: [[6, 10], 0], 10: [[6, 8], 0]}


# print(bfs(g, 1))

# print(input_graph)


def connected_comp(graph):
    all_con_comp = []
    for node in graph:
        if graph[node][1] == 0:
            all_con_comp.append(bfs(graph, node))

    return all_con_comp


print(bfs(input_graph, 1))
