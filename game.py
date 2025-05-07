from typing import Set
import string
from helpers import *


class Game:
    _secret_word: str = ""
    _guessed_letters: Set[str] = {'A', 'B'}
    _guesses_remaining: int = 1
    _current_round: int = 1
    _is_game_over = 0

    def start(self) -> None:
        self._secret_word = self.choose_secret_word()
        while not self._is_game_over:
            self.print_game_state()
            self.process_user_input()
            self._current_round += 1

    def process_user_input(self):
        while True:
            chosen_letter = input("Enter your guess: ")
            if len(chosen_letter) != 1 or chosen_letter not in string.ascii_letters:
                print("Please enter only one ascii character")
                continue
            if chosen_letter in self._guessed_letters:
                print("You already guessed this letter. Please choose a new one.")
                continue
            break

        if chosen_letter not in self._secret_word:
            self._guesses_remaining -= 1

        self._guessed_letters.add(chosen_letter)
        self.check_game_ending_conditions()

    def check_game_ending_conditions(self) -> None:
        if self._guesses_remaining < 1:
            self._is_game_over = True
            self.print_lost_menu()
        if '_' not in self.secret_word_display:
            self._is_game_over = True
            self.print_win_menu()

    # implement
    def choose_secret_word(self) -> str:
        return "hangman".upper()

    @property
    def available_letters(self) -> Set[str]:
        return set(string.ascii_uppercase) - self._guessed_letters

    @property
    def secret_word_display(self) -> str:
        _secret_word_display = self._secret_word
        for c in self.available_letters:
            _secret_word_display = _secret_word_display.replace(c, '_')
        return _secret_word_display

    def print_game_state(self) -> None:
        clear_console()
        lives_remaining = self._guesses_remaining if self._guesses_remaining > 3 else paint(
            str(self._guesses_remaining), Color.RED
        )
        print(f"Round {self._current_round}\t\t|\t\tLives remaining: {lives_remaining}")
        self.print_letters()
        print(self.secret_word_display)

    @property
    def secret_word_reveal_display(self) -> str:
        _secret_word_reveal_display = []
        for i in range(len(self._secret_word)):
            actual_letter = self._secret_word[i]
            guessed_letter = self.secret_word_display[i]
            reveal_letter = paint(actual_letter, Color.OKGREEN) if actual_letter == guessed_letter else actual_letter
            _secret_word_reveal_display.append(reveal_letter)
        return "".join(_secret_word_reveal_display)

    def print_lost_menu(self):
        you_lost_text = paint('You Lost!', Color.RED)
        print(f"{you_lost_text} The word was {self.secret_word_reveal_display}")

    def print_letters(self) -> None:
        all_letters = list(string.ascii_uppercase)
        strikethrough_character = '\u0336'
        for letter in all_letters:
            if letter in self._guessed_letters:
                color = Color.OKGREEN if letter in self._secret_word else Color.RED
                printable_letter = paint(letter + strikethrough_character, color)
            else:
                printable_letter = paint(letter, Color.OKCYAN)
            print(printable_letter, end=' ')
        print()


if __name__ == '__main__':
    game = Game()
    game.start()
