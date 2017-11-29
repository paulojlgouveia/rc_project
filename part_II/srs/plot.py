
import axelrod as axl
import matplotlib.pyplot as plt


def win_distribution(results, args = None):
	plot = axl.Plot(results)
	
	_, ax = plt.subplots()
	title = ax.set_title('Wins')
	xlabel = ax.set_xlabel('Strategies')
	
	img = plot.winplot(ax=ax)
	
	if args is not None:
		name = "../img/wins/wins"
		for arg in args:
			name += "-"+str(arg)
		name += ".png"
		img.savefig(name)
	
	return name, img
	
	

def payoff_distribution(results, args = None):
	plot = axl.Plot(results)
	
	_, ax = plt.subplots()
	title = ax.set_title('Payoff')
	xlabel = ax.set_xlabel('Strategies')
	
	img = plot.boxplot(ax=ax)
	
	if args is not None:
		name = "../img/payoff/payoff"
		for arg in args:
			name += "-"+str(arg)
		name += ".png"
		img.savefig(name)
	
	return name, img



def payoff_matrix(results, args = None):
	plot = axl.Plot(results)
	img = plot.payoff()
	
	if args is not None:
		name = "../img/matrix/matrix"
		for arg in args:
			name += "-"+str(arg)
		name += ".png"
		img.savefig(name)
	
	return name, img


