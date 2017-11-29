
import os, sys, random, copy, collections
import axelrod as axl
import matplotlib.pyplot as plt

from display import view_payoff_distribution, view_win_distribution, view_payoff_matrix, view_all_results
from display import Emphasis, print_numbered_list, get_unic_strs
from lists import clear_cmds, quit_cmds, exit_cmds


results_view = {
	"0": [view_payoff_distribution, "View payoff distribution"],
	"1": [view_win_distribution,    "View wins distribution"],
	"2": [view_payoff_matrix,       "View payoff distribution"],
	"3": [view_all_results,         "All of the above"],
}


def results_view_loop(results):
	while True:
		print("\nView final results:")
		print_numbered_list(results_view)
		
		try:
			in_cmd = input("\n-> ").split()
			cmd = in_cmd[0]
			args = in_cmd[1:]
			
			plt.close('all') # close all open plots
			
			results_view[cmd][0](results, args)
			
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
		op_r = 3
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
	
	results_view_loop(results)

	

def play_evolution(players, tournaments, args = None):
	
	if args == None or len(args) == 0:
		op_t = 10
		op_r = 3
		op_p = 10
	else:
		op_t = int(args[0])
		op_r = int(args[1])
		op_p = int(args[2])
	
	# create a population
	population = []
	for strategy in players:
		print(Emphasis.ITALIC  + "copying " + str(strategy) + Emphasis.END)
		for i in range(0, op_p):
			population.append(copy.deepcopy(strategy))
	
	scores = []
	
	title = Emphasis.BOLD + "Evolution: " + Emphasis.END
	terms = Emphasis.ITALIC + "\n  players per strategy = " + str(op_p) \
							+ "\n  total players = " + str(len(population)) \
							+ "\n  turns = " + str(op_t) \
							+ "\n  repetitions = " + str(op_r) + Emphasis.END
	print(title + terms)
	
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
			population[player1] = copy.deepcopy(population[player2])
			print(str(population[player1]), "=>", str(population[player2]))
			
		elif scores[player1] > scores[player2]:
			population[player2] = copy.deepcopy(population[player1])
			print(str(population[player2]), "=>", str(population[player1]))
			
		else:
			print("did not copy.")
		
	
	print("Count of strategies in the end:")
	count = collections.Counter([str(x) for x in population])
	for k,v in count.items():
		print("  ", v, k)

	results_view_loop(results)



def human_interaction(players, tournaments, args = None):
	
	print(Emphasis.ITALIC + Emphasis.UNDERLINE + "Interactive play:" + Emphasis.END)
	
	me = axl.Human(name='me')
	player_including_me = [players[n], me]
	
	match = axl.Match(player_including_me, turns=5)
	match.play()
	
