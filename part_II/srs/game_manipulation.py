import axelrod as axl
import pprint


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


def visualise_tournaments_game(tours):
    result_item = [item[1] for item in tours]
    for results in result_item:
        visualise_boxplot(results)
        visualise_win_distribution(results)
        visualise_payoff_matrix(results)
        input()


def summary_results(tours):
    result_item = [item[1] for item in tours]
    for results in result_item:
        summy = results.summarise()
        pprint.pprint(summy)


def interaction_results(tours):
    tournaments = [item[0] for item in tours]
    result_item = [item[1] for item in tours]
    for x in range(0, len(result_item) - 1):
        for index_pair, interaction in sorted(result_item[x].interactions.items()):
            player1 = tournaments[x].players[index_pair[0]]
            player2 = tournaments[x].players[index_pair[1]]
            print('%s vs %s: %s' % (player1, player2, interaction[0]))


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


def human_interation(players, n):
    me = axl.Human(name='me')
    player_including_me = [players[n], me]
    match = axl.Match(player_including_me, turns=5)
    match.play()
