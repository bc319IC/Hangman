# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Table of Contents
- Installation
- Usage
- File Structure
- License Information

## Installation
None, just clone the repository using the command `git clone
https://github.com/bc319IC/Hangman.git` in the terminal.

## Usage
Run the appropraite files in the following section regarding their descriptions by typing `python3` followed by the filename in the terminal.

## File Structure

### milestone_2.py

Checking if the input is valid.

### milestone_3.py

Checking if the guess character is in the word.

### milestone_4.py

Implementation of the Hangman class which takes in a word list to start the game.

### milestone_5.py

Completed version of the Hangman game against the computer with the default number of lives set to 5 with a word list already provided which can be altered before starting the program according to the user's needs. 

#### game logic

The hangman class consists of initialising the class attributes followed by two class functions of which one checks whether the guessed letter is a valid/repeated input and the other checks whether the guessed letter is in the word and changes the number of lives accordingly. Upon guessing the word or running out of lives, the game is ended.

## License Information
This project is licensed under the terms of the MIT license.