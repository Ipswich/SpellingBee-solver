# SpellingBee-solver

Not so much a solver as a helper, this script is for the Spelling Bee mobile app. Spelling Bee is a word game where a player is presented with 7 letters, one of which is required. The player then tries to create as many words as they can using the provided letters. A word is only valid if it is 4 or more characters and contains the required character. The length of the word dictates the amount of points it's worth.

This game can easily be approached as a brute forceable guessing game (basically the approach to checking if a word is valid).

This script functions by asking the user for input; first a single input for the required letter, then a string of 6 letters for optional letters. The script should print the largest word found and a list of all of the words found.