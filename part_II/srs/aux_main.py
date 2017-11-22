from game_manipulation import *


def print_numbered_list(list):
    for t in range(len(list)):
        print("  " + str(t).rjust(2) + "  " + list[t])


def tournament(players, n):
    tour = axl.Tournament(players, repetitions=n)  # Create a tournament
    results = tour.play(keep_interactions=True)  # Play the tournament
    return [tour, results]


def visualise_mode_init(tours):
    visualise_mode = ["Visualising the results of the tournament",
                      "Visualising the distributions of wins",
                      "Visualising the payoff matrix",
                      "All"]
    print_numbered_list(visualise_mode)
    cmd = input("\n-> ")
    if cmd == "0":
        visualise_boxplot(tours)
    elif cmd == "1":
        visualise_win_distribution(tours)
    elif cmd == "2":
        visualise_payoff_matrix(tours)
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


def human_interation_init(players):
    players_list = ["Cooperator",
                    "Defector",
                    "TitForTat",
                    "ForgivingTitForTat",
                    "Joss",
                    "ZDMem2",
                    "ZDExtort2",
                    "WinStayLoseShift",
                    "ZDGTFT2"]
    print("\nplayers:")
    print_numbered_list(players_list)
    cmd = input()
    human_interation(players, int(cmd))


def init():
    players = [axl.Cooperator(),
               axl.Defector(),
               axl.TitForTat(),
               axl.ForgivingTitForTat(),
               axl.Joss(),
               axl.ZDMem2(),
               axl.ZDExtort2(),
               axl.WinStayLoseShift(),
               axl.ZDGTFT2()]

    tours = [tournament(players, 1),
             tournament(players, 5),
             tournament(players, 25),
             tournament(players, 50),
             tournament(players, 100)]

    return players, tours
