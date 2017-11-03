
import networkx as nx


def load_graph(graphFile):
		
	if graphFile.endswith(".gml"):
		print("reading " + graphFile + " as a .gml file.\n")
		return nx.read_gml(graphFile)
		
	elif graphFile.endswith(".gexf"):
		print("reading " + graphFile + " as a .gexf file.\n")
		return nx.read_gexf(graphFile)
		
	elif graphFile.endswith(".graphml"):
		print("reading " + graphFile + " as a .graphml file.\n")
		return nx.read_graphml(graphFile)
		
	elif graphFile.endswith(".gephi"):
		print("reading " + graphFile + " as a .gephi file.\n")
		return get_gephi_graph(graphFile)
	
	
	print("failed to identify file type.")
	return None


	
def get_gephi_graph(graphFile):
	print("NOT IMPLEMENTED.\n")


