
tournament = "4"
evolution = "5"
evolution_2 = "6"
save = "5"
back = "q"
exit = "e"

#noise_list = [0.0, 0.1]
#turns_list = [10**x for x in range(0, 2)]
#repetitions_list = [10**x for x in range(0, 2)]
#players_list = range(1, 3)
#iterations_list = [10**x for x in range(0, 2)]

noise_list = [0.0, 0.1, 0.3, 0.6, 0.9]
turns_list = [10**x for x in range(0, 6)]
repetitions_list = [10**x for x in range(0, 6)]
players_list = range(1, 11)
iterations_list = [10**x for x in range(0, 6)]


########### tournaments ###########

for noise in noise_list:
	for turns in turns_list:
		for repetitions in repetitions_list:
			
			cmd = str(tournament) + " " + str(noise) + " " + str(turns) + " " + str(repetitions)
			
			print(cmd)
			print(save)
			print(back)



########### evolution ###########

for noise in noise_list:
	for turns in turns_list:
		for repetitions in repetitions_list:
			for players in players_list:
				for iterations in iterations_list:
					
					cmd = str(evolution) + " " + str(noise) \
						+ " " + str(turns) + " " + str(repetitions) \
						+ " " + str(players) + " " + str(iterations)
					
					print(cmd)
					print(save)
					print(back)



########### evolution 2 ###########

for noise in noise_list:
	for turns in turns_list:
		for repetitions in repetitions_list:
			for players in players_list:
				for iterations in iterations_list:
					
					cmd = str(evolution_2) + " " + str(noise) \
						+ " " + str(turns) + " " + str(repetitions) \
						+ " " + str(players) + " " + str(iterations)
					
					print(cmd)
					print(save)
					print(back)



print(exit)

