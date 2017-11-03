
import sys
import random
import networkx as nx
from networkx.exception import NetworkXError

from drawing import *

### Graph Generation Functions ###

# Return random graph using Barabasi-Albert preferential attachment model.
# The graph is grown by attaching new nodes with a given number of edges
# that are preferentially attached to existing nodes with high degree.

def barabasi_albert(args):
	
	# use default values if passed wrong arguments
	if len(args) != 3:
		nodes = 20
		edges = 3
		draw_mode = 0
		print("wrong format. expected: <nodes> <edges> <draw_mode>")
		print("using default values:", nodes, ",", edges, ",", draw_mode)
		
	else:
		nodes = int(args[0])
		edges = int(args[1])
		draw_mode = int(args[2])
	
	draw_set(draw_mode)
	
	# create new graph
	G = nx.Graph()
	for u in range(0, nodes):
		G.add_node(u)
		draw_set_pos(G, u, nodes)
	
	draw_update(G)

	# list of existing nodes, with nodes repeated once for each adjacent edge
	target_list = []

	# manually create edges for the first node
	for v in range(1, edges + 1):
		G.add_edge(0, v)
		target_list.append(0) # add source node to the list
		target_list.append(v) # add target node to the list
	
	draw_update(G)

	for u in range(1, nodes):
		
		for i in range(0, edges):
			# choose a target node (preferencial) it's not connected to and it's not itself
			v = random.choice(target_list)

			# if target is not itself and is not already connected
			if u != v and not G.has_edge(u, v):
				G.add_edge(u, v)
				target_list.append(u) # add source node to the list
				target_list.append(v) # add target node to the list
		
		draw_update(G)
		
	return G


# Return a random (connected) graph using Watts-Strogatz model.
# The graph is grown by rewiring existing edges with probability p,
# from a starting ring graph were each node is connected to its k neighbors

def watts_strogatz(args):
		
	# use default values if passed wrong arguments
	if len(args) != 4:
		nodes = 20
		edges = 4
		p = 0.5
		draw_mode = 0
		print("wrong format. expected: <nodes> <edges> <probability> <draw_mode>")
		print("using default values:", nodes, ",", edges, ",", p, ",", draw_mode)
		
	else:
		nodes = int(args[0])
		edges = int(args[1])
		p = float(args[2])
		draw_mode = int(args[3])

	draw_set(draw_mode)

	# repeat until we get a valid graph
	t = 0
	while t < 10:
		t += 0
		
		# create graph
		G = nx.Graph()
		for u in range(0, nodes):
			G.add_node(u)
			draw_set_pos(G, u, nodes)
		
		# connect each node to k/2 neighbors
		for u in range(0, nodes):
			for i in range(1, edges // 2 + 1):
				v = (u + i) % nodes
				G.add_edge(u, v)
	
		draw_clear()
		draw_update(G)
		draw_wait(1)
	
		# rewire edges with probability p
		for u in range(0, nodes):
			for i in range(1, edges // 2 + 1):
				v = (u + i) % nodes
				
				if random.random() < p:
					# choose a target node (random) that it's not connected to and its not itself
					w = random.randrange(0, nodes)
					while G.has_edge(u, w) or w == u:
						w = random.randrange(0, nodes)
						# if there are no possible nodes left
						if G.degree(u) >= nodes - 1:
							break
					
					G.remove_edge(u,v)
					G.add_edge(u,w)
					
		draw_clear()
		draw_update(G)
		
		# return graph if connected
		if nx.is_connected(G):
			return G
	
	print("Failed to generate a connected graph in the given number of tries. Exiting...")
	sys.exit()


# A random (connected) graph is grown by creating a fully connected graph of size n
# and adding "cloned" nodes one by one. Each "cloned" node has probability q of being
# connected to the original node and probability p of being connected to each of its neighbors.

def partial_duplication(args):
	
	# use default values if passed wrong arguments
	if len(args) != 5:
		N = 20
		n = 4
		p = 0.5
		q = 1
		draw_mode = 0
		print("wrong format. expected: \
			<nodes_fin> <nodes_ini> <p_join_neighbor> <p_join_source> <draw_mode>")
		print("using default values:", N, ",", n, ",", p, ",", q, ",", draw_mode)
	else:
		N = int(args[0])
		n= int(args[1])
		p = float(args[2])
		q = float(args[3])
		draw_mode = int(args[4])
	
	draw_set(draw_mode)

	# repeat until we get a valid graph
	t = 0
	while t < 100:
		t += 1
		
		# create complete graph with size n
		G = nx.Graph()
		for u in range(0, n):
			G.add_node(u)
			draw_set_pos(G, u, N)
			for v in range (0, u):
				G.add_edge(u, v)
		
		draw_clear()
		draw_update(G)
		draw_wait(1)
		
		for u in range(n, N):
			# create new "cloned" node
			G.add_node(u)
			draw_set_pos(G, u, N)
			
			# choose a target node (random) to be cloned
			v = random.randrange(0, u)
	
			# For each neighbor of u...
			for w in list(G.neighbors(v)):
				# connect it to target neighbor with probability p
				if random.random() < p:
					G.add_edge(u, w)
	
			# connect it to target with probability q
			if random.random() < q:
				G.add_edge(u, v)
					
			draw_update(G)
		
		# return graph if connected
		if nx.is_connected(G):
			return G
	
	print("Failed to generate a connected graph in the given number of tries. Exiting...")
	sys.exit()

