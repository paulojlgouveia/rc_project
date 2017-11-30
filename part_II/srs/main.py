
import os, sys
# check if running under python3
if sys.version_info < (3, 0):
	sys.stdout.write("DENIED: requires Python 3.x\n")
	sys.exit(1)
else:
	import axelrod as axl

from play import play_tournament, play_evolution, human_interaction
from display import print_strategies, print_players
from display import Emphasis, print_numbered_list
from lists import clear_cmds, quit_cmds, exit_cmds



def add_strategy(players, tournaments, args = []):
	print(Emphasis.BOLD + "Available strategies: " + Emphasis.END)
	print_numbered_list([str(x()) for x in axl.all_strategies])

	try:
		index = int(input("\n-> "))
		
		new = axl.all_strategies[index]()
		
		if new not in players:
			players.append(new)
			
		else:
			print("Strategy already in the list.")
		
	except ValueError as e:
		print("invalid index.")
		
	return players


def remove_strategy(players, tournaments, args = []):
	print(Emphasis.BOLD + "Strategies: " + Emphasis.END)
	print_numbered_list([str(x) for x in players])
	try:
		index = int(input("\n-> "))
		del(players[index])
		
	except ValueError as e:
		print("invalid index.")
	
	return players



def init_players():
	#players = [s() for s in axl.demo_strategies]
	players = [
		axl.Cooperator(),
		axl.Defector(),
		axl.TitForTat(),
		axl.GTFT(),
		axl.ForgivingTitForTat(),
		axl.Joss(),
		axl.WinStayLoseShift(),
		axl.ZDExtort2(),
		axl.ZDGTFT2(),
		axl.Random()
	]
	
	return players


def init_tournaments():
	tournaments = []
	return tournaments




execution_modes = {
	"1": [print_strategies,  "View strategies"],
	"2": [add_strategy,      "Add a strategy"],
	"3": [remove_strategy,   "Remove a strategy"],
	"4": [play_tournament,   "Tournament\t <noise> <turns> <repetitions>"],
	"5": [play_evolution,    "Evolution\t\t <noise> <turns> <repetitions> <players-per-strategy> <iteratirons>"],
	"6": [human_interaction, "Human interation\t <turns> <repetitions> <name>"]
}



def main():
	
	if not os.path.exists("../img/"):
		os.makedirs("../img/matrix/")
		os.makedirs("../img/payoff/")
		os.makedirs("../img/wins/")
	
	os.system("tput reset")

	players = init_players()
	tournaments = init_tournaments()
	
	
	while True:
		print("\nExecution mode:")
		print_numbered_list(execution_modes)
		
		try:
			in_cmd = input("\n-> ").split()
			cmd = in_cmd[0]
			args = in_cmd[1:]
			results = execution_modes[cmd][0](players, tournaments, args)
			
		#except IndexError as e:
			#continue
			
		except KeyError as e:
			if cmd in quit_cmds:
				break
				
			elif cmd in exit_cmds:
				sys.exit(0)
				
			elif cmd in clear_cmds:
				os.system("tput reset")
				
			else:
				print("invalid option.")
				continue
	


if __name__ == '__main__':
	main()

