import random
from typing import Set
import string
from helpers import *

MAX_GUESSES = 6  # it should be 6 for the hangman pictures to work


class Game:
    _number_of_games_won = 0
    _number_of_games_lost = 0
    _secret_word: str = ""
    _guessed_letters: Set[str] = set()
    _guesses_remaining: int = MAX_GUESSES
    _current_round: int = 1
    _is_game_over = False
    _is_new_game = True
    _did_guess_word = False
    _words = []

    def __init__(self):
        self.load_words()

    def start(self) -> None:
        print(self._is_new_game)
        while self._is_new_game:
            self.reset_game()
            while not self._is_game_over:
                self.print_game_state()
                self.process_user_input()
                self._current_round += 1

    def reset_game(self):
        self._guessed_letters: Set[str] = set()
        self._guesses_remaining: int = MAX_GUESSES
        self._current_round: int = 1
        self._is_game_over = False
        self._secret_word = self.choose_secret_word()
        self._is_new_game = False
        self._did_guess_word = False

    def process_user_input(self):
        while True:
            chosen_letter = input("Enter your guess: ").upper()
            if chosen_letter.startswith(">"):
                self._did_guess_word = True
                chosen_word = chosen_letter[1:]
                if chosen_word == self._secret_word:
                    self._number_of_games_won += self.secret_word_display.count('_')
                    for c in self._secret_word:
                        self._guessed_letters.add(c)
                    break
                else:
                    self._guesses_remaining = 0
                    break
            if len(chosen_letter) != 1 or chosen_letter not in string.ascii_uppercase:
                print("Please enter only one ascii character")
                continue
            if chosen_letter in self._guessed_letters:
                print("You already guessed this letter. Please choose a new one.")
                continue
            break

        if not self._did_guess_word and chosen_letter not in self._secret_word:
            self._guesses_remaining -= 1

        self._guessed_letters.add(chosen_letter)
        self.check_game_ending_conditions()

    def check_game_ending_conditions(self) -> None:
        if self._guesses_remaining < 1:
            self._is_game_over = True
            self._number_of_games_lost += 1
            self.print_lost_menu()
        if '_' not in self.secret_word_display:
            self._is_game_over = True
            self._number_of_games_won += 1
            self.print_win_menu()
        if self._is_game_over:
            self.print_overall_game_score()
            self.prompt_new_game()

    def prompt_new_game(self):
        underlined_Y = paint('Y', Color.UNDERLINE)
        underlined_N = paint('N', Color.UNDERLINE)
        while True:
            is_new_game = input(f"Do you want to play a new game? {underlined_Y}es/{underlined_N}o: ").upper()
            if is_new_game in ('YES', 'Y'):
                self._is_new_game = True
                break
            elif is_new_game in ('NO', 'N'):
                break
            print(f"Please enter either {underlined_Y}es or {underlined_N}o")

    def load_words(self):
        with open('words.txt', 'r') as words_file:
            self._words = words_file.read().split('\n')

    # implement
    def choose_secret_word(self) -> str:
        secret_word = random.choice(self._words).upper()
        return secret_word

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
        self.print_hangman()
        lives_remaining = self._guesses_remaining if self._guesses_remaining > 3 else paint(
            str(self._guesses_remaining), Color.RED
        )
        print(f"Round {self._current_round}\t\t|\t\tLives remaining: {lives_remaining}")
        self.print_letters()
        print(f"> {self.secret_word_display} <")

    @property
    def secret_word_reveal_display(self) -> str:
        _secret_word_reveal_display = []
        for i in range(len(self._secret_word)):
            actual_letter = self._secret_word[i]
            guessed_letter = self.secret_word_display[i]
            reveal_letter = paint(actual_letter, Color.GREEN) if actual_letter == guessed_letter else actual_letter
            _secret_word_reveal_display.append(reveal_letter)
        return "".join(_secret_word_reveal_display)

    def print_hangman(self):
        hangman_picture_index = MAX_GUESSES - self._guesses_remaining
        print(HANGMANPICS[hangman_picture_index])

    def print_lost_menu(self):
        clear_console()
        self.print_hangman()
        you_lost_text = paint('You Lost!', Color.RED)
        print(f"{you_lost_text} The word was {self.secret_word_reveal_display}")

    def print_win_menu(self):
        clear_console()
        print(HANGMAN_SAVED_PIC)
        you_won_text = paint('You Won!', Color.GREEN)
        print(f"{you_won_text} The word was {self.secret_word_reveal_display}")

    def print_overall_game_score(self):
        wins = paint(f"won {self._number_of_games_won} games", Color.GREEN)
        loses = paint(f"lost {self._number_of_games_lost} games", Color.RED)
        to_print = f"You {wins} and {loses}"
        print(to_print)

    def print_letters(self) -> None:
        all_letters = list(string.ascii_uppercase)
        for letter in all_letters:
            if letter in self._guessed_letters:
                color = Color.GREEN if letter in self._secret_word else Color.RED
                printable_letter = paint(paint(letter, color), Color.STRIKE)
            else:
                printable_letter = paint(letter, Color.CYAN)
            print(printable_letter, end=' ')
        print()
