import random
import copy


# from math import inf

# def merge(rand1, rand2, dict):
#     for ind, item in enumerate(dict):
#         if ind + 1 == rand1:

# new_list = list(filter((rand1).__ne__, item))

# ensure nodes are connected
def get_valid_nodes(graph):
    v1 = graph.keys()[random.randint(0, len(graph) - 1)]
    v2 = graph[v1][random.randint(0, len(graph[v1]) - 1)]
    return v1, v2


def min_cut(input_dict):
    while len(input_dict) > 2:
        v1, v2 = get_valid_nodes(input_dict)
        # Remove vertex 2 from vertex 1
        node1 = [x for x in input_dict[v1] if x != v2]

        # Remove vertex 1 from vertex 2
        input_dict[v2] = [y for y in input_dict[v2] if y != v1]

        # Vertex elements to vertex 2
        input_dict[v2].extend(node1)

        # Delete vertex 1
        input_dict = {k: v for k, v in input_dict.iteritems() if k != v1}

        # Replace vertex 1 with vertex 2 in adjacency the list
        for ind, item in input_dict.items():
            input_dict[ind] = [v2 if z == v1 else z for z in item]

    return input_dict


test = {1: [2, 4], 2: [1, 3, 4], 3: [2, 4], 4: [1, 2, 3]}

input_graph = {int(line.rstrip().split()[0]): [int(i) for i in line.rstrip().split()[1:]] for line in
               open("../test_files/graphs/kt_min_copy.txt")}

minc = 100

for ind in range(100):
    # make sure to load the file for each run (or make a copy)
    grap = copy.deepcopy(input_graph)
    dict = min_cut(grap)
    print(len(dict.items()[0][1]), len(dict.items()[1][1]))

print minc
