
import axelrod as axl
import matplotlib.pyplot as plt

class Emphasis:
	PURPLE = '\033[95m'
	BLUE = '\033[94m'
	CYAN = '\033[96m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	ITALIC = '\x1B[3m'
	
	END = '\033[0m'


def print_numbered_list(bag):	
	if isinstance(bag, dict):
		for k, v in sorted(bag.items()):
			print("  " + str(k).rjust(2) + "  " + v[1])
		
	elif isinstance(bag, list):
		for t in range(len(bag)):
			print("  " + str(t).rjust(2) + "  " + bag[t])


def get_unic_strs(bag):
	output = []
	seen = set()
	
	for thing in bag:
		if str(thing) not in seen:
			output.append(str(thing))
			seen.add(str(thing))
	
	return output


def print_strategies(players, tournaments, args = None):
	print(Emphasis.ITALIC + Emphasis.UNDERLINE + "Strategies:" + Emphasis.END)
	for s in get_unic_strs(players):
		print("    " + s)


def print_players(players, tournaments, args = None):
	print(Emphasis.ITALIC + Emphasis.UNDERLINE + "Players:" + Emphasis.END)
	for p in players:
		print("    " + str(p))




def view_win_distribution(results, args = None):
	plot = axl.Plot(results)
	
	_, ax = plt.subplots()
	title = ax.set_title('Wins')
	xlabel = ax.set_xlabel('Strategies')
	
	img = plot.winplot(ax=ax)
	
	if args is not None:
		name = "../img/wins"
		for arg in args:
			name += "-"+str(arg)
		name += ".png"
		img.savefig(name)
	
	img.show()
	
	

def view_payoff_distribution(results, args = None):
	plot = axl.Plot(results)
	
	_, ax = plt.subplots()
	title = ax.set_title('Payoff')
	xlabel = ax.set_xlabel('Strategies')
	
	img = plot.boxplot(ax=ax)
	
	if args is not None:
		name = "../img/payoff"
		for arg in args:
			name += "-"+str(arg)
		name += ".png"
		img.savefig(name)
	
	img.show()



def view_payoff_matrix(results, args = None):
	plot = axl.Plot(results)
	img = plot.payoff()
	
	if args is not None:
		name = "../img/matrix"
		for arg in args:
			name += "-"+str(arg)
		name += ".png"
		img.savefig(name)
	
	img.show()



def view_all_results(results, args = None):
	view_payoff_distribution(results, args)
	view_win_distribution(results, args)
	view_payoff_matrix(results, args)




