
import sys



def main():
	
	# check if running under python3
	if sys.version_info < (3, 0):
		sys.stdout.write("DENIED: requires Python 3.x\n")
		sys.exit(1)
	
	


if __name__ == '__main__':
	main()
	
	