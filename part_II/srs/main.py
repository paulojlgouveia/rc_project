
import sys
import axelrod as axl
import _tkinter


def main():
	
	# check if running under python3
	if sys.version_info < (3, 0):
		sys.stdout.write("DENIED: requires Python 3.x\n")
		sys.exit(1)
	
	
	axl.seed(0)  # Set a seed
	players = [s() for s in axl.all_strategies]  # Create players
	tournament = axl.Tournament(players)  # Create a tournament
	results = tournament.play()  # Play the tournament
	
	print(results.ranked_names)
	
	


if __name__ == '__main__':
	main()
	
	