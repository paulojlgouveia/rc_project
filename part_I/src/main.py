
import sys
from os import listdir
from os.path import isfile, join

import networkx as nx


from graph_loading import load_graph
from drawing import *
from graph_generation import *
from metrics import print_desired_metrics


def help():
	print("\n" + "-"*90)
	
	print("usage:")
	print("\tpython3 main.py [options]")
	
	print("\noptions:")
	print("\t-a\tanalyse a graph file")
	print("\t-g\tgraph generation [default behaviour]")
	#print("\t-d\tdraw the graph per iteration of its generation")
	#print("\t-p\tplot the degree distribution")
	print("\t-h\thelp")
	
	print("\ncontrols:")
	print("\t#\tselect option")
	print("\tq\tback")
	print("\te\texit")
	
	print("-"*90)
	
	
	
def print_numbered_list(list):
	for t in range(len(list)):
		print("  " + str(t).rjust(2) + "  " + list[t])



def get_available_graphs(datasetsDirectory):
	
	return [f for f in listdir(datasetsDirectory) if isfile(join(datasetsDirectory, f))]




def graph_file_analysis_loop():
	
	datasetsDirectory = "../datasets/"
	
	graphFiles = get_available_graphs(datasetsDirectory)
	
	while True:
		print("\navailable graph files:")
		print_numbered_list(graphFiles)
		
		cmd = input("\n-> ").split()
		
		if cmd[0] == "q" or cmd[0] == "quit":
			break
		
		elif cmd[0] == "e" or cmd[0] == "exit":
			sys.exit(1)
		
		graphFile = graphFiles[int(cmd[0])]
		
		print("selected: " + graphFile + "\n")
		G = load_graph(datasetsDirectory + graphFile)
		print_desired_metrics(G)
		draw_update(G)



def graph_generation_loop():
	
	models = ["Barabasi Albert", "Watts Strogatz", "Node Duplication"]
	
	function_dictionary = {
		"0": barabasi_albert,
		"1": watts_strogatz,
		"2": partial_duplication
	}
	
	while True:
		print("\ngraph generation models:")
		print_numbered_list(models)
		
		try:
			# choose a function from the ones available and give it a list with the args
			cmd = input("\n-> ").split()
			G = function_dictionary[cmd[0]](cmd[1:])
			
		except KeyError as e:
			if cmd[0] == "q" or cmd[0] == "quit":
				break
				
			elif cmd[0] == "e" or cmd[0] == "exit":
				sys.exit(1)
				
			else:
				print("invalid option.")
				continue
			
		draw_wait(1)
		draw_clear()
		
		print_desired_metrics(G)
		
		draw_close()



def main():
	
	# check if running under python3
	if sys.version_info < (3, 0):
		sys.stdout.write("DENIED: requires Python 3.x\n")
		sys.exit(1)
	
	
	# flags were used (execute and quit)
	if len(sys.argv) > 1:
		
		if "-h" in sys.argv:
			help()
		
		if len(sys.argv) == 2:
			
			if sys.argv[1] == "-g":
				graph_generation_loop()
				
			elif sys.argv[1] == "-a":
				graph_file_analysis_loop()
			
		#for f in sys.argv[1:]:
			#G = load_graph(datasetsDirectory + f)
			#print_desired_metrics(G)
		
		
	# interactive mode (no flags)
	else:
		help()
		
		draw_setup()
		
		modes = ["graph generation", "graph file analysis"]
		
		while True:
			print("\nexecution mode:")
			print_numbered_list(modes)
			
			cmd = input("\n-> ")
			
			if cmd == "0":
				graph_generation_loop()
				
			elif cmd == "1":
				graph_file_analysis_loop()
				
			elif cmd == "q" or cmd == "quit":
				break
			
			elif cmd == "e" or cmd == "exit":
				sys.exit(1)
				
			else:
				continue
			
		print("queue the XP shutdown theme.\n")
	
	
	
if __name__ == '__main__':
	main()
	
# else:
#	main.py is being imported and not run
	
	
	
