#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random

pWins = 0
cWins = 0
totalTies = 0

def get_player_move():
    """Asks the user to enter a move as 'r', 'p', or 's', and return it"""
    return raw_input("Choose your move: r, p, or s").lower()

def get_computer_move():
    """Randomly generates the computer's move and
    returns it in the form of 'r', 'p', or 's'"""
    return "rps"[random.randint(0,2)]


def determine_winner(player_move, comp_move):
    """Takes in a player move and computer move each as 'r', 'p', or 's',
    and returns the winner as 'player', 'computer', or 'tie'"""


def print_scoreboard(player_wins, comp_wins, ties):
    """Prints out the scoreboard neatly.  Returns nothing."""


def get_move_name(short_move):
    """Takes in 'r', 'p', or 's', and returns 'Rock', 'Paper, or
    'Scissors' respectively. Use this to neatly print move choices"""


# Write your code below - make RPS happen using the functions above!

roundsToPlay = raw_input("How many rounds to play? ")

for round in range(0, int(roundsToPlay)):
    playerMove = get_player_move()

    while playerMove != 'r' and playerMove != 'p' and playerMove != 's':
        print("Incorrect input, please input a correct value.")
        playerMove = get_player_move()

    computerMove = get_computer_move()

    winner = determine_winner(playerMove, computerMove)

    print(" ")
    print(winner + " wins")

    print_scoreboard(pWins, cWins, totalTies)