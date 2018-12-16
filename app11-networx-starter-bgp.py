# Networkx Base Functionality
# Mapping nodes using BGP AS Number
# Exercises from Bodenseo
# Tested in Python 3.7
# Current test result:

import networkx as nx
import matplotlib as plt


def program_header():
    print("--------------------------------------------")
    print("           NETWORKX BASIC                   ")
    print("--------------------------------------------")
    print()


def env_test():
    testnet = nx.Graph()
    testnet.add_node("65210")
    testnet.add_nodes_from(["65211", "65471"])

    testnet.add_edge("65210", "65211")
    testnet.add_edge("65210", "65471")
    testnet.add_edge("65211", "65471")

    print("Nodes of graph: ")
    print(testnet.nodes())
    print("Edges of graph: ")
    print(testnet.edges())
    return testnet


def env_test_display(testnet):
    nx.draw(testnet)
    plt.savefig("simple_path.png")  # save as png
    plt.show()  # display



def main():
    program_header()
    testnet=env_test()
#   env_test_display(testnet)


if __name__ == "__main__":
    main()
