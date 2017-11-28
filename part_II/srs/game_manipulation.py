from pprint import pprint
import axelrod as axl
import random


def visualise_boxplot(tours):
    result_item = [item[1] for item in tours]
    for results in result_item:
        plot = axl.Plot(results)
        p = plot.boxplot()
        p.show()
        input()


def visualise_win_distribution(tours):
    result_item = [item[1] for item in tours]
    for results in result_item:
        plot = axl.Plot(results)
        p = plot.winplot()
        p.show()
        input()


def visualise_payoff_matrix(tours):
    result_item = [item[1] for item in tours]
    for results in result_item:
        plot = axl.Plot(results)
        p = plot.payoff()
        p.show()
        input()


def visualise_tournaments_game(tours):
    visualise_boxplot(tours)
    visualise_win_distribution(tours)
    visualise_payoff_matrix(tours)
    input()


def summary_results(tours):
    result_item = [item[1] for item in tours]
    for results in result_item:
        summy = results.summarise()
        pprint(summy)


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


def evolution():
    '''players = [s() for s in axl.cheating_strategies] + [axl.Cooperator(),
                                                        axl.Defector(),
                                                        axl.TitForTat(),
                                                        axl.ForgivingTitForTat(),
                                                        axl.Joss(),
                                                        axl.WinStayLoseShift(),
                                                        axl.ZDExtort2(),
                                                        axl.ZDGTFT2(),
                                                        axl.Random()]


    players = [s() for s in axl.all_strategies]
    new = players[:]
    deleted = [axl.Adaptive().__class__,
               axl.Resurrection().__class__,
               axl.Geller().__class__,
               axl.MetaHunter().__class__]
    for x in range(0, len(new)):
        if new[x].__class__ in deleted:
            del players[x]'''

    players = [axl.Cooperator(),
                axl.Defector(),
                axl.TitForTat(),
                axl.ForgivingTitForTat(),
                axl.Joss(),
                axl.WinStayLoseShift(),
                axl.ZDExtort2(),
                axl.ZDGTFT2(),
                axl.Random()]

    for x in range(0, len(players)*100):
        player1 = random.randint(0, len(players) - 1)
        player2 = random.randint(0, len(players) - 1)
        player_match = [players[player1], players[player2]]
        match = axl.Match(player_match, 100)
        match.play()
        score = match.final_score()
        if score[0] > score[1]:
            players[player2] = players[player1]

        else:
            players[player1] = players[player2]
    print(players)
