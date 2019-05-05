# interpreter test for grave

import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.approximation.dominating_set import min_weighted_dominating_set

from grave import plot_network

network = nx.powerlaw_cluster_graph(55, 1, .2)
"""
Parameter examples:
10,2,.1 almost bowtie
50, 1, .2 Doc example - multi hub and spoke
51,1,.2 two hubs start connecting
52,1,.2 split universe
53 or 54,1,.2 starburst with offshoots
55,1,.2 interconnected clusters - path management essential
52,2,.3 near-symmetrical constellation

50, 12, .4 more symmetrical, dense web
"""
dom_set = min_weighted_dominating_set(network)

for node, node_attrs in network.nodes(data=True):
    node_attrs['is_dominator'] = True if node in dom_set else False

def color_dominators(node_attrs):
    if node_attrs.get('is_dominator', False):
        return {'color': 'red'}
    else:
        return {'color': 'green'}

fig, ax = plt.subplots()
plot_network(network, node_style=color_dominators)
plt.show()