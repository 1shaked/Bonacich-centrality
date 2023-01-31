import numpy as np

import networkx as nx

# Create a sample graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1,2), (2,3), (3,4), (4,5)])

# Get the adjacency matrix
A = nx.adjacency_matrix(G)
adj = A.toarray()
centrality = np.dot(A,A).toarray()
print(centrality)
# Calculate the sum of the elements in each row of the power centrality matrix and store the result in a vector.
row_sum = np.sum(centrality, axis=1)
# normalize 
total_of_row = sum(row_sum)

row_sum_normalized = row_sum * 1/total_of_row

print('Bonacich centrality sores are')
for index, el in enumerate(row_sum_normalized):
    print(f'index - {index} is {el}')
