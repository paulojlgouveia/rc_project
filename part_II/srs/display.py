
import axelrod as axl
import matplotlib.pyplot as plt

from plot import win_distribution, payoff_distribution, payoff_matrix

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
			print(" " + str(k).rjust(3) + "  " + v[1])
		
	elif isinstance(bag, list):
		for t in range(len(bag)):
			print(" " + str(t).rjust(3) + "  " + bag[t])


def get_unic_strs(bag):
	output = []
	seen = set()
	
	for thing in bag:
		if str(thing) not in seen:
			output.append(str(thing))
			seen.add(str(thing))
	
	return output


def print_strategies(players, tournaments, args = None):
	print(Emphasis.BOLD + "Strategies: " + Emphasis.END)
	for s in get_unic_strs(players):
		print("    " + s)


def print_players(players, tournaments, args = None):
	print(Emphasis.BOLD + "Players: " + Emphasis.END)
	for p in players:
		print("    " + str(p))




def view_win_distribution(results, args = None):
	_, img = win_distribution(results, args)
	img.show()
	
	

def view_payoff_distribution(results, args = None):
	_, img = payoff_distribution(results, args)
	img.show()



def view_payoff_matrix(results, args = None):
	_, img = payoff_matrix(results, args)
	img.show()



def view_all_results(results, args = None):
	view_payoff_distribution(results, args)
	view_win_distribution(results, args)
	view_payoff_matrix(results, args)



def save_results(results, args = None):
	name1, img1 = win_distribution(results, args)
	name2, img2 = payoff_distribution(results, args)
	name3, img3 = payoff_matrix(results, args)
	
	img1.savefig(name1)
	img2.savefig(name2)
	img3.savefig(name3)



