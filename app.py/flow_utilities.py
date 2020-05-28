import random
import json
import flow_visualize

def generate_flow_network(n = "random"):
    """Generates a flow network WITH MAXIMUM POSSIBLE EDGES using a two dimentional array ,
    if n --> number of nodes is not specified, by default it will generate
    a flow network with at least 6 and a maximum of 10 nodes
    """

    if n == "random":
        n = random.randint(6,10)
    flow_network = [[0 for i in range(n)] for j in range(n)]   #initalize 2D array with a array with all 0 for a the given size
    for i in range(n):
        for j in range(n):
            if i != j :
                flow_network[i][j]= random.randint(10,100)
            if i == n-1:
                flow_network[i][j] = 0
    return flow_network

def generate_flow_network_given_links(n, links, r1=10,r2=100):
    """Generates a flow network with given number of links where links connected in order
    (from starting link to ending link)using a two dimentional array , if the n --> number of nodes is not
    specified by default it will generate a flow network with at least 6 and a maximum of 10 nodes
    """
    flow_network = [[0 for i in range(n)] for j in range(n)]
    counter = 0
    for i in range(n):
        for j in range(n):
            if i != j :
                flow_network[i][j]= random.randint(r1,r2)
                counter += 1
            if links == counter:
                return flow_network

def generate_flow_randomly(n,links):
    """Generates a flow network with given number of links where links connected RANDOMLY
    (* there is possibility for source and sink not to be connected  based on params.)
    a two dimentional array , if the n --> number of nodes is not
    specified by default it will generate a flow network with at least 6 and a maximum of 10 nodes
    """
    flow_network = [[0 for i in range(n)] for j in range(n)]
    counter =0
    while counter < links:
        ran1 = random.randint(0,n-1)
        ran2 = random.randint(0,n-1)
        if(flow_network[ran1][ran2] != 0 or ran1 != ran2):
            flow_network[ran1][ran2] = random.randint(10,100)
            counter+=1
    return flow_network

def delete_node_from_network(flow_network, node):
    """ Deletes a the node of given flow network denoted by a 2D array and returns the new
        flow network denoted by the 2D array
    """
    size = len(flow_network[0])
    for i in range(size):
        for j in range(size):
            if j ==  node:
                flow_network[i].pop(j)
    flow_network.pop(node)
    return flow_network


def delete_link_from_network(flow_network, node1, node2):
    """ Deletes a the link(capacity) between two nodes ( node1 and node2) of given flow network denoted by a 2D array and returns the new
        flow network denoted by the 2D array
    """
    flow_network[node1][node2] = 0
    return flow_network

def modify_link_from_network(flow_network, node1,node2,new_capacity):
    """ Modify the capacity between two given nodes in the flow network denoted by the 2d array
        and returns the newly updated flow network
    """
    flow_network[node1][node2] = new_capacity
    return flow_network


def return_flow_network_from_file(filename):
    """returns network array when dataa name is given"""
    f = open(filename, "r")
    f.readline()
    enc_flow_array = f.readline()
    flow_network = json.loads(enc_flow_array)
    f.close()
    return flow_network

def create_flow_dataset(filename,flow_size):
    "Creating single data set with given name and maximum number of edges given the nodes"
    f = open(filename,"w")
    flow_network = generate_flow_network(flow_size)
    enc_flow_network = json.dumps(flow_network)
    f.write(enc_flow_network)
    f.close()

def create_multiple_datasets(start_nodes,start_links,number_of_datasets):
    """Create a set of data , with the specified amount of start nodes and links which are
        doubled each time for the amount of iterations specified
    """
    for i in range(number_of_datasets):
        dataset_name = "dataset-"+str(i)
        flow_network = generate_flow_network_given_links(start_nodes,start_links)
        enc_flow_network = json.dumps(flow_network)
        f = open(dataset_name, "w")
        f.write(str(start_links)+"\n")
        f.write(enc_flow_network)
        f.close()
        start_links = start_links * 2
        start_nodes = start_nodes * 2



