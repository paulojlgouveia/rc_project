
import os, sys, random, copy, collections
import axelrod as axl
import matplotlib.pyplot as plt

from display import view_payoff_distribution, view_win_distribution, view_payoff_matrix, view_all_results
from display import Emphasis, print_numbered_list, get_unic_strs
from lists import clear_cmds, quit_cmds, exit_cmds


results_view = {
	"0": [view_win_distribution,    "View wins distribution"],
	"1": [view_payoff_distribution, "View payoff distribution"],
	"2": [view_payoff_matrix,       "View payoff matrix"],
	"3": [view_all_results,         "View all of the above"],
	#"4": [save_results,             "Save all plots"],
}


def results_view_loop(results, terms):	
	while True:
		print("\nView final results:")
		print_numbered_list(results_view)
		
		try:
			in_cmd = input("\n-> ").split()
			cmd = in_cmd[0]
			args = in_cmd[1:]
			
			plt.close('all') # close all open plots
			
			results_view[cmd][0](results, terms)
			
		except IndexError as e:
			continue
			
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



def play_tournament(players, tournaments, args = []):
	if args == None or len(args) == 0:
		op_t = 10
		op_r = 1000
	else:
		op_t = int(args[0])
		op_r = int(args[1])
	
	
	title = Emphasis.BOLD + "Tournament: " + Emphasis.END
	terms = Emphasis.ITALIC + "\n  players = " + str(len(players)) \
							+ "\n  turns = " + str(op_t) \
							+ "\n  repetitions = " + str(op_r) + Emphasis.END
	print(title + terms)
	
	# create and play a tournament
	tournament = axl.Tournament(players, turns=op_t, repetitions=op_r)
	results = tournament.play(keep_interactions=True, processes=0)
	
	results_view_loop(results, [op_t, op_r])

	

def play_evolution(players, tournaments, args = None):
	
	if args == None or len(args) == 0:
		op_t = 10
		op_r = 2
		op_p = 10
		op_i = len(players)*op_p
	else:
		op_t = int(args[0])
		op_r = int(args[1])
		op_p = int(args[2])
		op_i = int(args[3])
	
	title = Emphasis.BOLD + "Evolution: " + Emphasis.END
	terms = Emphasis.ITALIC + "\n  turns = " + str(op_t) \
							+ "\n  repetitions = " + str(op_r) \
							+ "\n  players per strategy = " + str(op_p) \
							+ "\n  total players = " + str(len(players)*op_p) + Emphasis.END
	print(title + terms)
	
	# create a population
	population = []
	for strategy in players:
		print(Emphasis.ITALIC  + "copying " + str(strategy) + Emphasis.END)
		for i in range(0, op_p):
			population.append(copy.deepcopy(strategy))
	
	print()
	scores = []
	
	
	# play an arbitrary number of tournaments
	for i in range(0, len(population)):
		
		# play a tournament
		tournament = axl.Tournament(population, turns=op_t, repetitions=op_r)
		results = tournament.play(keep_interactions=True, processes=0)
		scores = results.normalised_scores
		
		# pick two random players
		player1 = random.randrange(0, len(population))
		player2 = random.randrange(0, len(population))
		
		# compare payoffs and copy strategies
		if scores[player1] < scores[player2]:
			print(str(population[player1]), " => ", str(population[player2]))
			population[player1] = copy.deepcopy(population[player2])
			
		elif scores[player1] > scores[player2]:
			print(str(population[player2]), " => ", str(population[player1]))
			population[player2] = copy.deepcopy(population[player1])
			
		else:
			print("did not copy.")
		
	
	print(Emphasis.BOLD + "\nCount of strategies in the end:" + Emphasis.END)
	count = collections.Counter([str(x) for x in population])
	for k,v in count.items():
		print(str(v).rjust(3), k)

	results_view_loop(results, [op_t, op_r, op_p])



def human_interaction(players, tournaments, args = None):
	
	if args == None or len(args) == 0:
		op_t = 4
		op_r = 1
		op_name = "You"
	else:
		op_t = int(args[0])
		op_r = int(args[1])
		name = args[2]
	
	title = Emphasis.BOLD + "Interactive play: " + Emphasis.END
	terms = Emphasis.ITALIC + "\n  turns = " + str(op_t) \
							+ "\n  repetitions = " + str(op_r) \
							+ "\n  name = " + op_name + Emphasis.END
	print(title + terms)
	
	print(Emphasis.ITALIC + Emphasis.UNDERLINE + "Interactive play:" + Emphasis.END)
	
	me = axl.Human(name=op_name)
	player_including_me = players + [me]
	
	print(player_including_me)
	tournament = axl.Tournament(player_including_me, turns=op_t, repetitions=op_r)
	results = tournament.play(keep_interactions=True)


