# graph
# req: pip install networkx

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)  # add one node
G.add_nodes_from([2, 3])  # add nodes from iterable
G.add_nodes_from([(4, {"color": "red"})])  # add node with atribute

G.add_edge(1, 2)
G.add_edges_from([(3, 4)])

nx.draw(G, with_labels=True)
plt.show()
