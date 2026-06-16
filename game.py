import random
from words import WORDS


class HangmanGame:

    HANGMAN_PICS = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]

    def __init__(self):
        self.category = None
        self.word = ""
        self.guessed = set()
        self.attempts = 6
        self.score = 0

    def choose_category(self):

        categories = list(WORDS.keys())

        print("\nChoose Category:\n")

        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")

        while True:
            try:
                choice = int(input("\nEnter choice: "))

                if 1 <= choice <= len(categories):
                    self.category = categories[choice - 1]
                    self.word = random.choice(
                        WORDS[self.category]
                    ).lower()
                    break

                print("Invalid choice.")

            except ValueError:
                print("Please enter a number.")

    def display_word(self):

        return " ".join(
            letter if letter in self.guessed else "_"
            for letter in self.word
        )

    def guess_letter(self):

        while True:

            letter = input(
                "\nEnter a letter: "
            ).lower()

            if len(letter) != 1 or not letter.isalpha():
                print("Enter a single alphabet.")
                continue

            if letter in self.guessed:
                print("Already guessed.")
                continue

            return letter

    def update_game(self, letter):

        self.guessed.add(letter)

        if letter not in self.word:
            self.attempts -= 1
            print("Wrong guess!")
        else:
            print("Correct!")

    def is_won(self):

        return all(
            letter in self.guessed
            for letter in self.word
        )

    def play(self):

        self.choose_category()

        while self.attempts > 0:

            print(
                self.HANGMAN_PICS[
                    6 - self.attempts
                ]
            )

            print(
                f"\nCategory: {self.category}"
            )

            print(
                f"Attempts Left: {self.attempts}"
            )

            print(
                f"Score: {self.score}"
            )

            print(
                "\nWord:",
                self.display_word()
            )

            letter = self.guess_letter()

            self.update_game(letter)

            if self.is_won():

                self.score += 10

                print("\nCongratulations!")
                print(
                    f"You guessed '{self.word}'"
                )

                print(
                    f"Final Score: {self.score}"
                )
                return

        print(
            self.HANGMAN_PICS[-1]
        )

        print("\nGame Over!")
        print(
            f"The word was: {self.word}"
        )