
import os, sys, math, random, copy, collections
import axelrod as axl
import matplotlib.pyplot as plt

from display import *
from lists import *


results_view = {
	"1": [view_win_distribution,    "View wins distribution"],
	"2": [view_payoff_distribution, "View payoff distribution"],
	"3": [view_payoff_matrix,       "View payoff matrix"],
	"4": [view_all_results,         "View all of the above"],
	"5": [save_results,             "Save all plots"],
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
		op_n = 0.0
		op_t = 200
		op_r = 2
	else:
		op_n = float(args[0])
		op_t = int(args[1])
		op_r = int(args[2])
	
	
	title = Emphasis.BOLD + "Tournament: " + Emphasis.END
	terms = Emphasis.ITALIC + "\n  players = " + str(len(players)) \
							+ "\n  turns = " + str(op_t) \
							+ "\n  repetitions = " + str(op_r) \
							+ "\n  noise = " + str(op_n) + Emphasis.END + "\n"
	print(title + terms)
	
	# create and play a tournament
	tournament = axl.Tournament(players, turns=op_t, repetitions=op_r, noise=op_n)
	results = tournament.play(keep_interactions=True, processes=0)
	
	results_view_loop(results, ["_t_", 'n'+str(op_n), 't'+str(op_t), 'r'+str(op_r)])



def play_evolution(players, tournaments, args = None):
	
	if args == None or len(args) == 0:
		op_n = 0.0
		op_t = 10
		op_r = 2
		op_p = 10
		op_i = len(players)*op_p
	else:
		op_n = float(args[0])
		op_t = int(args[1])
		op_r = int(args[2])
		op_p = int(args[3])
		op_i = int(args[4])
	
	title = Emphasis.BOLD + "Evolution: " + Emphasis.END
	terms = Emphasis.ITALIC + "\n  turns = " + str(op_t) \
							+ "\n  repetitions = " + str(op_r) \
							+ "\n  players per strategy = " + str(op_p) \
							+ "\n  total players = " + str(len(players)*op_p) \
							+ "\n  interactions = " + str(op_i) \
							+ "\n  noise = " + str(op_n) + Emphasis.END + "\n"
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
	for i in range(0, op_i):
		
		# play a tournament
		tournament = axl.Tournament(population, turns=op_t, repetitions=op_r, noise=op_n)
		results = tournament.play(keep_interactions=True, processes=0)
		scores = results.normalised_scores
		
		# pick two random players
		p1 = random.randrange(0, len(population))
		p2 = random.randrange(0, len(population))
		
		if population[p1] != population[p2]:
			
			f_p1 = scores[p1][0]
			f_p2 = scores[p2][0]
			
			# compare payoffs and copy strategies
			if f_p1 < f_p2:
				print(i, ':', Emphasis.ITALIC + str(population[p1]) + " => " + str(population[p2]) + Emphasis.END)
				population[p1] = copy.deepcopy(population[p2])
				
			elif f_p1 > f_p2:
				print(i, ':', Emphasis.ITALIC + str(population[p2]) + " => " + str(population[p1]) + Emphasis.END)
				population[p2] = copy.deepcopy(population[p1])
				
			else:
				print(i, ':', Emphasis.ITALIC + "Did not copy: same fitness." + Emphasis.END)
				
		else:
			print(i, ':', Emphasis.ITALIC + "Did not copy: same strategy." + Emphasis.END)
		
		
	print(Emphasis.BOLD + "\nCount of strategies at the end:" + Emphasis.END)
	count = collections.Counter([str(x) for x in population])
	for k,v in count.items():
		print(str(v).rjust(3), k)

	results_view_loop(results, ["_e_", 'n'+str(op_n), 't'+str(op_t), 'r'+str(op_r), 'p'+str(op_p), 'i'+str(op_i)])




def play_evolution_2(players, tournaments, args = None):
	
	if args == None or len(args) == 0:
		op_n = 0.0
		op_t = 100
		op_r = 2
		op_p = 10
		op_i = len(players)*op_p
	else:
		op_n = float(args[0])
		op_t = int(args[1])
		op_r = int(args[2])
		op_p = int(args[3])
		op_i = int(args[4])
	
	title = Emphasis.BOLD + "Evolution v2: " + Emphasis.END
	terms = Emphasis.ITALIC + "\n  turns = " + str(op_t) \
							+ "\n  repetitions = " + str(op_r) \
							+ "\n  players per strategy = " + str(op_p) \
							+ "\n  total players = " + str(len(players)*op_p) \
							+ "\n  interactions = " + str(op_i) \
							+ "\n  noise = " + str(op_n) + Emphasis.END + "\n"
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
	for i in range(0, op_i):
		
		# play a tournament
		tournament = axl.Tournament(population, turns=op_t, repetitions=op_r, noise=op_n)
		results = tournament.play(keep_interactions=True, processes=0)
		scores = results.normalised_scores
		
		
		if i % 100 == 0:
			save_results(results, ["_ev2_", 'n'+str(op_n), 't'+str(op_t), 'r'+str(op_r), 'p'+str(op_p), 'i'+str(i)])
		
		
		p1 = random.randrange(0, len(population))
		
		if random.random() < 1/len(population):
			new_strategy = players[random.randrange(0, len(players))]
			print(i, ':', Emphasis.ITALIC + str(population[p1]) + " => " + str(new_strategy) + Emphasis.END)
			population[p1] = copy.deepcopy(new_strategy)
			
		else:
			p2 = random.randrange(0, len(population))
			
			if population[p1] != population[p2]:
				f_p1 = scores[p1][0]
				f_p2 = scores[p2][0]
				
				beta = 1
				prob = 1 / (1 + math.exp(-beta * (f_p2 - f_p1)))
				
				if random.random() < prob:
					print(i, ':', Emphasis.ITALIC + str(population[p1]) + " => " + str(population[p2]) + Emphasis.END)
					population[p1] = copy.deepcopy(population[p2])
					
				else:
					print(i, ':', Emphasis.ITALIC + "Did not copy: missed probability check." + Emphasis.END)
				
			else:
				print(i, ':', Emphasis.ITALIC + "Did not copy: same strategy." + Emphasis.END)
		
	
	print(Emphasis.BOLD + "\nCount of strategies at the end:" + Emphasis.END)
	count = collections.Counter([str(x) for x in population])
	for k,v in count.items():
		print(str(v).rjust(3), k)

	results_view_loop(results, ["_ev2_", 'n'+str(op_n), 't'+str(op_t), 'r'+str(op_r), 'p'+str(op_p), 'i'+str(op_i)])





def human_interaction(players, tournaments, args = None):
	
	if args == None or len(args) == 0:
		op_t = 4
		op_r = 1
		op_name = "You"
	else:
		op_t = int(args[0])
		op_r = int(args[1])
		op_name = args[2]
	
	title = Emphasis.BOLD + "Interactive play: " + Emphasis.END
	terms = Emphasis.ITALIC + "\n  turns = " + str(op_t) \
							+ "\n  repetitions = " + str(op_r) \
							+ "\n  name = " + op_name + Emphasis.END + "\n"
	print(title + terms)
	
	print(Emphasis.ITALIC + Emphasis.UNDERLINE + "Interactive play:" + Emphasis.END)
	
	me = axl.Human(name=op_name)
	player_including_me = players + [me]
	
	print(player_including_me)
	tournament = axl.Tournament(player_including_me, turns=op_t, repetitions=op_r)
	results = tournament.play(keep_interactions=True)

	results_view_loop(results, ["_h_", 't'+str(op_t), 'r'+str(op_name), 'n'+str(op_name)])

