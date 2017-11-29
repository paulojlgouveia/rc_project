
from game_manipulation import *


def print_numbered_list(list):
    for t in range(len(list)):
        print("  " + str(t).rjust(2) + "  " + list[t])


def tournament(players, n):
    tour = axl.Tournament(players, repetitions=n)  # Create a tournament
    results = tour.play(keep_interactions=True, processes=0)  # Play the tournament
    return [tour, results]


def visualise_mode_init(tours):
    visualise_mode = ["View the results of the tournament",
                      "View the distributions of wins",
                      "View the payoff matrix",
                      "All"]

    print_numbered_list(visualise_mode)
    cmd = input("\n-> ")
    if cmd == "0":
        visualise_boxplot(tours)
		
    elif cmd == "1":
        visualise_win_distribution(tours)
		
    elif cmd == "2":
        visualise_payoff_matrix(tours)
		
    elif cmd == "q" or cmd == "b":
        return
		
    else:
        visualise_tournaments_game(tours)


def accessing_mode_init(tours):
    accessing_mode = ["View detailed interaction results",
                      "View all winners of each match"]

    print_numbered_list(accessing_mode)
    cmd = input("\n-> ")
    if cmd == "0":
        interaction_results(tours)

    elif cmd == "1":
        view_winners(tours)

    elif cmd == "q" or cmd == "b":
        return


def human_interation_init(players):
    players_list = ["Cooperator",
                    "Defector",
                    "TitForTat",
                    "ForgivingTitForTat",
                    "Joss",
                    "WinStayLoseShift",
                    "ZDExtort2",
                    "ZDGTFT2",
                    "Random"]
    print("\nplayers:")
    print_numbered_list(players_list)
    cmd = input("\n-> ")
    human_interation(players, int(cmd))


def init():
    players = [axl.Cooperator(),
               axl.Defector(),
               axl.TitForTat(),
               axl.ForgivingTitForTat(),
               axl.Joss(),
               axl.WinStayLoseShift(),
               axl.ZDExtort2(),
               axl.ZDGTFT2(),
               axl.Random()]

    tournaments = []
    for k in range(1):
        n = 10 ** k
        print("\n-> players: " + str(len(players)) + ", repetitions: " + str(n))
        tournaments.append(tournament(players, n))

    return players, tournaments
