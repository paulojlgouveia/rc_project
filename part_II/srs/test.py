
tournament = "4"
evolution = "5"
save = "5"
back = "q"
exit = "e"


#noise_list = [0.0, 0.1, 0.2, 0.5, 0.9]
#turns_list = [10**x for x in range(0, 7)]
#repetitions_list = [10**x for x in range(0, 7)]
#players_list = range(1, 11)
#iterations_list = [10**x for x in range(0, 5)]


noise_list = [0.0, 0.1]
turns_list = [10**x for x in range(0, 2)]
repetitions_list = [10**x for x in range(0, 2)]
players_list = range(1, 3)
iterations_list = [10**x for x in range(0, 2)]



########### tournaments ###########

## varying noise
for noise in noise_list:
	
	## varying turns
	for turns in turns_list:
		
		## varying repetitions
		for repetitions in repetitions_list:
			cmd = str(tournament) + " " + str(noise) + " " + str(turns) + " " + str(repetitions)
			
			print(cmd)
			print(save)
			print(back)
		
	



########### evolution ###########

## varying noise
for noise in noise_list:
	
	## varying turns
	for turns in turns_list:
		
		## varying repetitions
		for repetitions in repetitions_list:
			
			## varying players per turn
			for players in players_list:
				
				## varying repetitions
				for iterations in iterations_list:
					
					cmd = str(evolution) + " " + str(noise) \
						+ " " + str(turns) + " " + str(repetitions) \
						+ " " + str(players) + " " + str(iterations)
					
					print(cmd)
					print(save)
					print(back)
				
			
		



print(exit)

