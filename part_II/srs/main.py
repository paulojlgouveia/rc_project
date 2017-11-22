import sys
import axelrod as axl
import pprint


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


def tournament(players, n):
    tour = axl.Tournament(players, repetitions=n)  # Create a tournament
    results = tour.play(keep_interactions=True)  # Play the tournament
    return [tour, results]


def tournaments_game(tours):
    result_item = [item[1] for item in tours]
    for results in result_item:
        visualise_boxplot(results)
        visualise_win_distribution(results)
        visualise_payoff_matrix(results)
        input()


def view_winners(tours):
    tournaments = [item[0] for item in tours]
    result_item = [item[1] for item in tours]
    for x in range(0, len(result_item) - 1):
        matches = []
        for index_pair, interaction in sorted(result_item[x].interactions.items()):
            player1 = tournaments[x].players[index_pair[0]]
            player2 = tournaments[x].players[index_pair[1]]
            match = axl.Match([player1, player2])
            match.result = interaction[0]
            matches.append(match)
        for match in matches:
            print("{} v {}, winner: {}".format(match.players[0], match.players[1], match.winner()))


def view_strategy(tours):
    tournaments = [item[0] for item in tours]
    result_item = [item[1] for item in tours]
    for x in range(0, len(result_item) - 1):
        for index_pair, interaction in sorted(result_item[x].interactions.items()):
            player1 = tournaments[x].players[index_pair[0]]
            player2 = tournaments[x].players[index_pair[1]]
            print('%s vs %s: %s' % (player1, player2, interaction[0]))


def visualise_boxplot(results):
    plot = axl.Plot(results)
    p = plot.boxplot()
    p.show()


def visualise_win_distribution(results):
    plot = axl.Plot(results)
    p = plot.winplot()
    p.show()


def visualise_payoff_matrix(results):
    plot = axl.Plot(results)
    p = plot.payoff()
    p.show()


def summary_results(results):
    summy = results.summarise()
    pprint.pprint(summy)


def main():
    # check if running under python3
    if sys.version_info < (3, 0):
        sys.stdout.write("DENIED: requires Python 3.x\n")
        sys.exit(1)

    players, tours = init()
    tournaments_game(tours)
    view_winners(tours)
    view_strategy(tours)


if __name__ == '__main__':
    main()
