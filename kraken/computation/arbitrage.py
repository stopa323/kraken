import kraken.computation.dummy_data as data
import matplotlib.pyplot as plt
import networkx as nx
from kraken.computation import utils

G = nx.DiGraph()
G.add_nodes_from(data.NODES_CYCLE)
G.add_weighted_edges_from(utils.log_weight(data.EDGES_CYCLE))

if nx.negative_edge_cycle(G):
    profitable = utils.cycle_filter(nx.simple_cycles(G),
                                    data.EDGES_CYCLE,
                                    max_cycle=3,
                                    min_cycle=3)
    for c, p in profitable:
        print("Profit for cycle %s: %s" % (c, p))
else:
    print('No negative cycle found')

d = G.get_edge_data('USD', 'ETH')
print(d)
# for c in nx.simple_cycles(G):
#     print(c)
# nx.draw(G, with_labels=True)
# plt.show()
