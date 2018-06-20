import kraken.computation.dummy_data as data
import matplotlib.pyplot as plt
import networkx as nx
from kraken.computation import utils


def get_profitable_chain(nodes, edges):
    """Returns arbitrage opportunity if one exists."""
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(utils.log_weight(edges))

    if nx.negative_edge_cycle(G):
        profitable = utils.cycle_filter(nx.simple_cycles(G),
                                        data.EDGES_CYCLE,
                                        max_cycle=6,
                                        min_cycle=1)
        for c, p in profitable:
            print("Profit for cycle %s: %s" % (c, p))
    else:
        print('No negative cycle found')

# for c in nx.simple_cycles(G):
#     print(c)
    nx.draw(G, with_labels=True)
    plt.show()

