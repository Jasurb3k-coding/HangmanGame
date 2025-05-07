# Welcome to Hangman
Get the latest version on [GitHub](https://github.com/Jasurb3k-coding/HangmanGame)

## Running the game
Run the game by
```shell
  python main.py
```

You will see:

```
  +---+
  |   |
      |
      |
      |
      |
=========
Round 1		|		Lives remaining: 6
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
> _________ <
Enter your guess: 
```

- State of the hanger
- Current round & Number of lives remaining
- The state of all the possible letters 
  - <span style="color:cyan">not guessed</span>
  - <span style="color:green">guessed correctly</span>
  - <span style="color:red">guessed incorrectly</span>
- State of the `secret word`, where `_` means the letter is not guessed and `A-Z` means the letter has been guessed.
- Prompt to enter your guess
  - You shall enter only one ascii character or the entire word following `>` (example: `>galaxy`)
  - The system is NOT case sensitive: you can enter both the letter or the full word in any case you want
  - Any error will be shown with a proper error message and prompts you again



## Rounds
Each guess is a one round.
- If a __correct word__ is guessed, a player moves on to the next round __without consequences__.
- If the __wrong letter__ is guessed, a player loses __1 life__.
- If a __wrong word__ is guessed, a player loses __all lives__ and automatically loses the game.   
- If a __correct word__ is guessed, a player gets __as many points as the number of missing letters__. (for example, guessing `h_ngm_n`, would give 2 points)
- If a player runs out of lives, he loses 1 point
- If a player guesses all the letters, he gains 1 point

# Bonus features
-[x] Words are loaded from the `words.txt` file. It can be modified to expand the game
-[x] Hangman graphic is drawn before each round and after winning or losing the game
-[x] Functionality to guess full words
-[ ] Difficulty levels 
-[x] Display number of games won/lost
-[x] Colors are used to easily distinguish important information.
  -[x] For guessed letters
  -[x] If remaining lives drop below 3