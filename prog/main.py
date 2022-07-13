from copy import deepcopy
from networkx.generators.random_graphs import erdos_renyi_graph
import networkx as nx
import time

def is_it_clique(gr):
    answers = [1 if len(x) == len(gr.keys()) - 1 else 0  for x in gr.values()]

    for answer in answers:
        if answer == 0:
            return 0


    return 1

'''n = 800
p = 0.05
g = erdos_renyi_graph(n, p)

print("Edges", len(g.edges))'''

graph = {}

graph = {"A": ["B", "C", "D"],
        "B": ["A", "C", "D", "E", "F", "G"],
        "C": ["A", "B", "D", "F", "I", "H", "K"],
        "D": ["A", "B", "C", "G", "J", "H", "K"],
        "E": ["F", "I", "G", "J"],
        "F": ["B", "C", "E"],
        "G": ["B", "D", "E"],
        "H": ["C", "D", "E", "I", "J", "K"],
        "I": ["C", "E", "H"],
        "J": ["D", "E", "H"],
        "K": ["C", "D", "H"]
        }

'''for line in nx.generate_adjlist(g):
    list_adj = line.split(" ")
    el = list_adj[0]
    list_adj.pop(0)
    graph[el] = list_adj'''

'''for key in graph.keys():
    for key_1 in graph.keys():
        if key != key_1 and key in graph[key_1]:
            graph[key].append(key_1)'''



k = 1

i = 0

keys = graph.keys() 

start = time.time()

if is_it_clique(graph) == 1:
    print("Answer: ", len(graph.keys()) - 1)
    exit()

tree_width = 1

size_of_tree_decomposition = 0

min_vertex_queue = []


lengths = []
is_clique = 0

#print(len(list(graph.items())[0][1]))
#min_lengths = len(list(graph.items())[0][1])
#min_lengths_letter = "a"
for i, x in enumerate(graph.items()):
    lengths.append((x[0], len(x[1])))
    #if (min_lengths > lengths[i][1]) and (lengths[i][0] not in min_vertex_queue):
    #    min_lengths = lengths[i][1]
    #    min_lengths_letter = lengths[i][0]

lengths.sort(key=lambda x:x[1])

H_graph = deepcopy(graph)

s = []

n = 0


while True:
    size_of_tree_decomposition += 1
    if (is_it_clique(H_graph)):
        s.append(list(H_graph.keys()))
        n = size_of_tree_decomposition
        break
    else:
        v_i = "a"
        adjacent_edge_of_v_i = []
        find_clique = 0
        for letter, x in lengths:

            adjusted_vertices = []
            if letter in H_graph.keys():
                [adjusted_vertices.append(adj) for adj in H_graph[letter]]
            adjusted_vertices.append(letter)
            graph_copy = deepcopy(H_graph)
            keys = graph_copy.copy().keys()
            for key in keys:
                if key not in adjusted_vertices:
                    del graph_copy[key]
                    for x in graph_copy.keys():
                        if key in graph_copy[x]:
                            graph_copy[x].remove(key)
            if (len(graph_copy) != 0 and is_it_clique(graph_copy)):
                v_i = letter
                adjacent_edge_of_v_i = graph_copy[v_i]
                find_clique = 1
                break
        
        if find_clique == 0:
            s.append(list(H_graph.keys()))
            n = size_of_tree_decomposition
            break
        adjacent_edge_of_v_i.append(v_i)
        s.append(adjacent_edge_of_v_i)
        if len(adjacent_edge_of_v_i) > tree_width:
            tree_width = len(adjacent_edge_of_v_i)

        del H_graph[v_i]

        for x in H_graph.keys():
            if v_i in H_graph[x]:
                H_graph[x].remove(v_i)

        if (len(H_graph.keys()) == 0):
            n = size_of_tree_decomposition
            break

max_el = 0
for el in s:
    if len(el) > max_el or max_el == 0:
        max_el = len(el)

print(s)

print("tree_width ",  max_el - 1)

end = time.time()
print("Time of work: ", end - start)