import kraken.computation.dummy_data as data
import matplotlib.pyplot as plt
import networkx as nx


G = nx.DiGraph()
G.add_nodes_from(data.NODES)
G.add_weighted_edges_from(data.EDGES)

nx.draw(G, with_labels=True)
plt.show()
