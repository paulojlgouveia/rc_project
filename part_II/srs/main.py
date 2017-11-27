import sys

from aux_main import *


def main():
    # check if running under python3
    if sys.version_info < (3, 0):
        sys.stdout.write("DENIED: requires Python 3.x\n")
        sys.exit(1)

    players, tours = init()

    # interactive mode (no flags)
    main_modes = ["View results",
                  "Summarise tournament results",
                  "Access the interactions",
                  "Human interation",
                  "Evolution"]

    while True:
        print("\nexecution mode:")
        print_numbered_list(main_modes)
        cmd = input("\n-> ")
        if cmd == "0":
            visualise_mode_init(tours)

        elif cmd == "1":
            summary_results(tours)

        elif cmd == "2":
            accessing_mode_init(tours)

        elif cmd == "3":
            human_interation_init(players)

        elif cmd == "4":
            evolution()

        elif cmd == "q" or cmd == "quit":
            break

        elif cmd == "e" or cmd == "exit":
            sys.exit(0)

        else:
            continue

    print("queue the XP shutdown theme.\n")


if __name__ == '__main__':
    main()
