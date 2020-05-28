import flow_utilities
import flow_visualize
import FlowNetwork
import flow_analysis

if __name__ == "__main__":
    stop = False
    graph = []
    while(stop != True):
        print("1 - Generate flow network\n"
              "2 - Delete node from flow network\n"
              "3 - Delete link from network\n"
              "4 - Modify link from network\n"
              "5 - Run algorithm\n"
              "6 - Import dataset\n"
              "7 - Create dataset\n"
              "8 - Run Doubling hypothesis\n"
              "9 - Analyze datasets\n"
              "10 - Exit")
        print("Please enter option :")
        user_input = input()
        try:
            user_input = int(user_input)
            if(user_input<1 or user_input >10):
                print("invalid input, input must be numeric and between 1 to 7")
        except:
            print("invalid input, input must be numeric and between 1 to 7")
        if(user_input == 1):
            print("1 - Generate flow network with maximum possible edges(Links) given nodes\n"
                  "2 - Generate flow network given nodes and edges ( edges connected in order from start node )\n"
                  "3 - Generate flow network given nodes and edges ( edges connected randomly)")
            user_input2 =  input()
            user_input2 = int(user_input2)
            if(user_input2 == 1):
                print("Please enter number of nodes :")
                nodes = int(input())
                graph = flow_utilities.generate_flow_network(nodes)
                flow_visualize.generate_graph(graph)
            elif(user_input2 == 2):
                print("Please enter number of nodes :")
                nodes = int(input())
                print("Please enter number of edges(links)")
                links = int(input())
                graph = flow_utilities.generate_flow_network_given_links(nodes,links)
                flow_visualize.generate_graph(graph)
            elif(user_input2 == 3):
                print("Please enter number of nodes :")
                nodes = int(input())
                print("Please enter number of edges(links)")
                links = int(input())
                graph = flow_utilities.generate_flow_randomly(nodes,links)
                flow_visualize.generate_graph(graph)
        if (user_input == 2):
                print("Enter node you want to delete :")
                node = int(input())
                graph = flow_utilities.delete_node_from_network(graph,node)
                flow_visualize.generate_graph(graph)
        if (user_input == 3):
            print("Enter nodes between link you want to delete :")
            print("Enter first node :")
            node1 = int(input())
            print("Enter second node :")
            node2 = int(input())
            graph = flow_utilities.delete_link_from_network(graph, node1,node2)
            flow_visualize.generate_graph(graph)
        if(user_input == 4):
            print("Enter nodes between link you want to modify and the new value :")
            print("Enter first node :")
            node1 = int(input())
            print("Enter second node :")
            node2 = int(input())
            print("Enter new capacity :")
            new_capacity = int(input())
            graph = flow_utilities.modify_link_from_network(graph,node1,node2,new_capacity)
            flow_visualize.generate_graph(graph)
        if(user_input == 5):
            print("Source is 0 and Sink is "+str(len(graph)-1))
            flow_visualize.generate_graph(graph)
            graph_flow_network = FlowNetwork.Graph(graph)
            result =graph_flow_network.FordFulkerson(0,len(graph)-1)
            print("Maximum flow is : "+str(result[0]))
            flow_visualize.generate_flow_distribution(result[1])
        if (user_input == 6):
            print("Please enter name of data set to import graph(flow network)")
            file_name = input()
            graph = flow_utilities.return_flow_network_from_file(file_name)
            flow_visualize.generate_graph(graph)
        if (user_input == 7 ):
            print("Please enter start nodes,start link and number of datasets required")
            print("Enter start nodes :")
            start_nodes = int(input())
            print("Enter start edges :")
            start_edges =int(input())
            print("Number of datasets :")
            num = int(input())
            flow_utilities.create_multiple_datasets(start_nodes,start_edges,num)
        if(user_input == 8 ):
            print("1 - Run doubling hypothesis for edges vs time (doubling edges and nodes)\n"
                  "2 - Run doubling hypothesis for nodes vs time (doubling nodes having max possible edges) ")
            user_input3 = int(input())
            if(user_input3 == 1):
                print("Please enter starting number of nodes :")
                start_nodes = int(input())
                print("Please enter start links :")
                start_links = int(input())
                print("Please enter number of iterations required :")
                iterations = int(input())
                flow_analysis.doubling_hypo_analysis_time_v_edges(start_nodes,start_links,iterations,3)
            elif(user_input3 == 2):
                print("Please enter starting number of nodes :")
                start_nodes = int(input())
                print("Please enter number of iterations required :")
                iterations = int(input())
                flow_analysis.doubling_hypo_analysis_time_v_nodes(start_nodes,iterations,3)
        if (user_input == 9):
            print("Enter amount of data sets to analyze")
            number = int(input())
            flow_analysis.analyse_multiple_datasets(number)
        if(user_input == 10):
            stop = True
            break;