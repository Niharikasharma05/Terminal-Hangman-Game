from game import HangmanGame


def main():

    while True:

        game = HangmanGame()

        game.play()

        choice = input(
            "\nPlay Again? (y/n): "
        ).lower()

        if choice != "y":
            print(
                "\nThanks for playing!"
            )
            break


if __name__ == "__main__":
    main()