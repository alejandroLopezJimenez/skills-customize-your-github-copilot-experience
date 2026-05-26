
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Implement Word Selection

#### Description
Set up the game by implementing a mechanism to randomly select a word from a predefined list.

#### Requirements
Completed program should:

- Randomly select words from a predefined list
- Store the selected word for the game
- Allow for future expansion with more words

### 🛠️ Handle Letter Guesses and Display Progress

#### Description
Implement the core guessing mechanism that accepts user input, validates guesses, and displays the current state of the word with underscores for unrevealed letters.

#### Requirements
Completed program should:

- Accept letter guesses from the user
- Show current progress in (_ _ _ format)
- Track which letters have been guessed
- Validate user input

### 🛠️ Track Game State and End Conditions

#### Description
Manage the game flow by tracking remaining attempts, determining win/lose conditions, and displaying appropriate messages.

#### Requirements
Completed program should:

- Track incorrect guesses remaining
- End the game when the word is guessed
- End the game when attempts are exhausted
- Display appropriate win/lose messages
