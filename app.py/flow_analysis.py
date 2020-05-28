import flow_utilities
import FlowNetwork
import time
from flow_visualize import generate_graph
import matplotlib.pyplot as plt
from tabulate import tabulate
import json
import math

def test_ford_fulk_given_size_max_links(size):
    array_graph = flow_utilities.generate_flow_network(size)

    graph = FlowNetwork.Graph(array_graph)
    source = 0
    sink = size - 1

    num_iter = 1   #number of iterations to magnify time taken
    start_time = time.process_time_ns()
    for i in range(num_iter):
        res = graph.FordFulkerson(source,sink)
    time_elapsed = time.process_time_ns() - start_time
    return time_elapsed,res[0]

def average_time_of_given_test_max_links(size, n=10):

    result_array = []
    avg_max_flow = []
    for i in range(n):
        result_array.append(test_ford_fulk_given_size_max_links(size)[0])
        avg_max_flow.append(test_ford_fulk_given_size_max_links(size)[1])
    avg_time = sum(result_array)/(len(result_array))
    avg_max_flow = sum(avg_max_flow)/(len(avg_max_flow))
    return avg_time,avg_max_flow

def doubling_hypo_analysis_time_v_nodes(start_nodes,iterations, refine):
    result_array = []
    nodes_array = []
    tab_array = []
    for i in range(iterations):
        result = average_time_of_given_test_max_links(start_nodes,refine)
        avg_time = result[0]/(10**6)
        result_array.append(avg_time)
        nodes_array.append(start_nodes*start_nodes)
        links = start_nodes * (start_nodes -1) - start_nodes
        avg_max_flow = result[1]
        if(avg_time != 0 and i > 0):
            if(tab_array[i-1][3] != 0):
                ratio = avg_time/tab_array[i-1][3]
                lg_ratio = math.log2(ratio)
        else:
            ratio = "-"
            lg_ratio ="-"
        tab_array.append([start_nodes,links,avg_max_flow,avg_time, ratio, lg_ratio])
        start_nodes = start_nodes * 2
    plt.title("FordFulkerson doubling hypothesis")
    plt.xlabel("input size (number of nodes)")
    plt.ylabel("time taken (ms)")
    plt.plot(nodes_array, result_array)
    print(tabulate(tab_array,["Nodes","edges","AVG max flow","AVG time","ratio","log2 ratio"],tablefmt="plain"))
    plt.show()
"""------------------------------------------------------------------------------------------------------"""


def test_ford_fulk_given_link_nodes(start_nodes, start_links):
    array_graph = flow_utilities.generate_flow_randomly(start_nodes, start_links)
    graph = FlowNetwork.Graph(array_graph)
    source = 0
    sink = start_nodes - 1
    num_iter = 1 #number of iterations to magnify time taken
    start_time = time.process_time_ns()
    for i in range(num_iter):
        res = graph.FordFulkerson(source,sink)
    time_elapsed = time.process_time_ns() - start_time
    return time_elapsed,res[0]

def average_of_given_test_doubling_size_links(start_nodes, start_links,accuracy):
    result_array = []
    avg_max_flow = []
    for i in range(accuracy):
        result_array.append(test_ford_fulk_given_link_nodes(start_nodes, start_links)[0])
        avg_max_flow.append(test_ford_fulk_given_link_nodes(start_nodes, start_links)[1])
    avg_time = sum(result_array)/(len(result_array))
    avg_max_flow = sum(avg_max_flow)/(len(avg_max_flow))
    return avg_time,avg_max_flow

def doubling_hypo_analysis_time_v_edges(start_nodes,start_links,iterations, refine):
    result_array = []
    index_array = []
    tab_array = []
    for i in range(iterations):
        result = average_of_given_test_doubling_size_links(start_nodes,start_links,refine)
        avg_time = result[0]/(10**6)
        result_array.append(avg_time)
        index_array.append(start_links)
        result = list(result)
        avg_max_flow = result[1]
        if(avg_time != 0 and i>0):
            if(tab_array[i-1][3] != 0):
                ratio = avg_time/tab_array[i-1][3]
                lg_ratio = math.log2(ratio)
        else:
            ratio = "-"
            lg_ratio ="-"
        tab_array.append([start_nodes,start_links,avg_max_flow,avg_time, ratio, lg_ratio, start_links*avg_max_flow])
        start_nodes = start_nodes*2
        start_links = start_links*2
    plt.title("FordFulkerson doubling hypothesis")
    plt.xlabel("input size (number of links)")
    plt.ylabel("time taken (ms)")
    plt.plot(index_array, result_array)
    print(tabulate(tab_array,["Nodes","edges","AVG max flow","AVG time(ms)","ratio","log2 ratio","avg_maxflow*links"],tablefmt="plain"))
    plt.show()
"""----------------------------------------------------------------------------------------------------------------------"""

def doubling_edges_constant_nodes(start_nodes,start_links,iterations, refine):
    result_array = []
    index_array = []
    tab_array = []
    for i in range(iterations):
        result = average_of_given_test_doubling_size_links(start_nodes,start_links,refine)
        avg_time = result[0]/(10**6)
        result_array.append(avg_time)
        index_array.append(start_links)
        result = list(result)
        avg_max_flow = result[1]
        if(avg_time != 0 and i>0):
            if(tab_array[i-1][3] != 0):
                ratio = avg_time/tab_array[i-1][3]
                lg_ratio = math.log2(ratio)
        else:
            ratio = "-"
            lg_ratio ="-"
        tab_array.append([start_nodes,start_links,avg_max_flow,avg_time, ratio, lg_ratio])
        start_links = start_links*2
    plt.title("FordFulkerson doubling hypothesis")
    plt.xlabel("input size (number of links)")
    plt.ylabel("time taken (ms)")
    plt.plot(index_array, result_array)
    print(tabulate(tab_array,["Nodes","edges","AVG max flow","AVG time(ms)","ratio ","log2 ratio"],tablefmt="plain"))
    plt.show()


def analyse_multiple_datasets(num_datasets):
    tab_array = []
    result_array = []
    edges_array = []
    for i in range(num_datasets):
        f = open("dataset-" + str(i), "r")
        num_links = f.readline()
        enc_flow_array = f.readline()
        flow_network = json.loads(enc_flow_array)
        f.close()

        flow_network_graph = FlowNetwork.Graph(flow_network)
        start_time = time.process_time_ns()
        result = flow_network_graph.FordFulkerson(0,len(flow_network)-1)
        time_elapsed = time.process_time_ns() - start_time
        time_elapsed_ms =time_elapsed/(10**6)
        edges_array.append(int(num_links))
        result_array.append(time_elapsed_ms)
        if(time_elapsed != 0 ):
            if(tab_array[i-1][3] != 0):
                ratio = time_elapsed/tab_array[i-1][3]
        else:
            ratio = "-"
        tab_array.append(("dataset-"+str(i),num_links,result[0],time_elapsed_ms,ratio))
    plt.plot(edges_array, result_array)
    plt.show()
    print(tabulate(tab_array, ["dataset ", "edges","max flow","time taken(ms)","ratio"], tablefmt="plain"))

def doubling_nodes_constant_egdes(start_nodes,start_links,iterations, refine):
    result_array = []
    index_array = []
    tab_array = []
    for i in range(iterations):
        result = average_of_given_test_doubling_size_links(start_nodes,start_links,refine)
        avg_time = result[0]/(10**6)
        result_array.append(avg_time)
        index_array.append(start_nodes)
        result = list(result)
        avg_max_flow = result[1]
        if(avg_time != 0 and i>0):
            if(tab_array[i-1][3] != 0):
                ratio = avg_time/tab_array[i-1][3]
                lg_ratio = math.log2(ratio)
        else:
            ratio = "-"
            lg_ratio ="-"
        tab_array.append([start_nodes,start_links,avg_max_flow,avg_time, ratio, lg_ratio, start_nodes*avg_max_flow])
        start_nodes = start_nodes*2
    plt.title("FordFulkerson doubling hypothesis")
    plt.xlabel("input size (number of nodes)")
    plt.ylabel("time taken (ms)")
    plt.plot(index_array, result_array)
    print(tabulate(tab_array,["Nodes","edges","AVG max flow","AVG time(ms)","ratio","log2 ratio"],tablefmt="plain"))
    plt.show()

def doubling_flow_values_const_node_edges(nodes,edges, min_cap,max_cap,iterations):
    tab_array = []
    for i in range(iterations):
        array_graph = flow_utilities.generate_flow_network_given_links(nodes,edges,min_cap,max_cap)
        graph = FlowNetwork.Graph(array_graph)
        source = 0
        sink = nodes - 1
        start_time = time.process_time_ns()
        res = graph.FordFulkerson(source, sink)
        time_elapsed = time.process_time_ns() - start_time
        time_elapsed = time_elapsed/(10**6)
        if(time_elapsed != 0 and i>0):
            if(tab_array[i-1][3] != 0):
                ratio = time_elapsed/tab_array[i-1][3]
                lg_ratio = math.log2(ratio)
        else:
            ratio = "-"
            lg_ratio ="-"
        tab_array.append([nodes, edges, res[0], time_elapsed, ratio, lg_ratio])
        min_cap = min_cap*20
        max_cap = max_cap*20
    print(tabulate(tab_array,["Nodes", "edges", "max flow", " time(ms)", "ratio", "log2 ratio"],tablefmt="plain"))

if __name__ == "__main__":
    #doubling_hypo_analysis_time_v_edges(10,80,8,5)
    #doubling_edges_constant_nodes(400,800,7,2)
    #doubling_hypo_analysis_time_v_nodes(6,7,1)
    #doubling_nodes_constant_egdes(100,9800,7,1)
    doubling_flow_values_const_node_edges(100,9600,50,100,7)
