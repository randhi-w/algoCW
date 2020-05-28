import networkx as nx
import matplotlib.pyplot as plt


def generate_graph(graph):
    """Create visual representation of a flow network when a 2D array is given"""
    G = nx.DiGraph()
    for i in range(len(graph[0])):
        G.add_node(i)
    for i in range(len(graph[0])):
        for j in range(len(graph[0])):
            if graph[i][j] != 0:
                G.add_edge(i,j,length=graph[i][j])




    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
    edge_labels = dict([((u, v,), d['length'])
                        for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=1/len(graph[0]), font_size=7)
    plt.show()



def generate_flow_distribution(flow_graph):
    """Creates a visual presentation for the flow netowrk and how the flow goes along the paths"""
    reversed_graph = [[0 for i in range(len(flow_graph))] for j in range(len(flow_graph))]
    red_edges = []
    for i in range(len(flow_graph)):
        for j in range(len(flow_graph)):
            reversed_graph[i][j]=flow_graph[j][i]

    for i in range(len(flow_graph)):
        for j in range(len(flow_graph)):
            if(reversed_graph[i][j] < 0 ):
                reversed_graph[i][j] = 0
            elif (reversed_graph[i][j] != 0):
                red_edges.append((i, j))
    G = nx.DiGraph()
    for i in range(len(reversed_graph[0])):
        G.add_node(i)
    for i in range(len(reversed_graph[0])):
        for j in range(len(reversed_graph[0])):
            if reversed_graph[i][j] != 0:
                G.add_edge(i,j,length=reversed_graph[i][j])


    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                            node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='blue', arrows=True,arrowsize=20)
    edge_labels = dict([((u, v,), d['length'])
                        for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=1/len(flow_graph[0]), font_size=12)

    plt.show()

