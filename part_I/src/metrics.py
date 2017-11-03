
from __future__ import division

import matplotlib.pyplot as plt

import networkx as nx
from networkx.exception import NetworkXError

def print_dictionary(dictionary):
	for k, v in dictionary.items():
		#print(f"{k:<4} {v}")
		print("  " + str(k).rjust(5) + "   ", str(v))


def print_desired_metrics(G):

	print(nx.info(G))
	print("average_clustering_coefficient \t" + str(average_clustering_coefficient(G)))
	print("average_path_len \t\t" + str(average_shortest_path_len(G)))
	degree_distribution(G) #it's an image file
	
	#print("clustering_coefficient: ")
	#print_dictionary(clustering_coefficient(G))
	#print("average_degree \t\t\t" + str(average_degree(G)))
	#print("closeness " + str(closeness(G)))
	#print("node_betweenness " + str(node_betweenness(G)))
	#print("edge_betweenness " + str(edge_betweenness(G)))
	#print("diameter " + str(diameter(G)))
	#print("eigenvector_centrality " + str(eigenvector_centrality(G)))
	
	
	
def degree_distribution(G):
	degree_list = []
	for k in  G.nodes():
		degree_list.append(G.degree(k))
	degree_list.sort(reverse=True)
	# print "Degree sequence", degree_sequence
	dmax = max(degree_list)

	plt.loglog(degree_list, 'b-', marker='o')
	plt.title("Degree rank plot")
	plt.ylabel("degree")
	plt.xlabel("rank")

	# draw graph in inset
	plt.axes([0.45, 0.45, 0.45, 0.45])
	#Gcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0]
	#pos = nx.spring_layout(Gcc)
	plt.axis('off')
	#nx.draw_networkx_nodes(Gcc, pos, node_size=20)
	#nx.draw_networkx_edges(Gcc, pos, alpha=0.4)
	
	plt.show()
	
	
	
def clustering_coefficient(G):
	info = nx.info(G).split()
	if info[2] == 'MultiGraph':
		return nx.average_clustering(nx.Graph(G))
	else:
		return nx.clustering(G)
	
	

def average_clustering_coefficient(G):
	info = nx.info(G).split()
	if info[2] == 'MultiGraph':
		return nx.average_clustering(nx.Graph(G))
	else:
		return nx.average_clustering(G)
	
	

def average_shortest_path_len(G):
	#return nx.average_shortest_path_length(G)
	
	if G.is_directed():
		if not nx.is_weakly_connected(G):
			raise nx.NetworkXError("Graph is not connected.")
	else:
		if not nx.is_connected(G):
			raise nx.NetworkXError("Graph is not connected.")
		
	avg = 0.0
	for node in G:
		path_length = nx.single_source_shortest_path_length(G, node)
		avg += sum(path_length.values())
		
		#if node % 100 == 0:
			#print(node)
	
	n = len(G)
	
	return avg/(n*(n-1))




def average_degree(G):
	return 2*G.number_of_edges()/len(G)



def diameter(G):
	return nx.diameter(G)



def edge_betweenness(G):
	return nx.edge_betweenness_centrality(G)



def node_betweenness(G):
	return nx.betweenness_centrality(G)



def closeness(G):
	return nx.closeness_centrality(G)



def eigenvector_centrality(G):
	info = nx.info(G).split()
	if info[2] == 'MultiGraph':
		return nx.eigenvector_centrality(nx.Graph(G))
	else:
		return nx.eigenvector_centrality(G)


