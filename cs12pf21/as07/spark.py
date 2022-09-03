#!/usr/bin/env python3
"""
You shall write a Python program that acts as a case-insensitive search engine for the South Park
script files available on our server. The search query and any configuration options shall be
specified as command-line arguments. Arguments are expected to be formatted as follows:

c:CHARACTER_NAME(S) selects only lines spoken by the specified character. If multiple of these
    arguments are given, only lines spoken by any of the specified characters shall be printed.
e:EPISODE_NUMBER selects only lines spoken in the specified episode number. If multiple of these
    arguments are given, only lines spoken in any of the specified episode numbers shall be printed.
s:SEASON_NUMBER selects only lines spoken in the specified season. If multiple of these arguments
    are given, only lines spoken in any of the specified season numbers shall be printed.
All other arguments shall be considered elements of the query. Only lines containing all query
elements shall be printed.
The program shall print to standard output, in chronological order, all lines of dialog matching
the query and other options, in the same format as received in the script files.
"""

import sys
import os
seasons = []
episodes = []
characters = []
text = []

for argument in sys.argv[1:]:
    if len(argument) > 1 and argument[1] == ":":
        if argument[0].lower() == "s":
            seasons.append(argument[2:].lower())
        elif argument[0].lower() == "e":
            episodes.append(argument[2:].lower())
        elif argument[0].lower() == "c":
            characters.append(argument[2:].lower())
    else:
        text.append(argument.lower())

file_list = sorted(os.listdir("/srv/datasets/SouthParkData/by-season"))

for file in file_list:
    if file[-4:] == ".txt":
        try:
            with open("/srv/datasets/SouthParkData/by-season/" + file) as open_file:
                for line in open_file:
                    season, episode, character, speech = line.split("\t")
                    if not season.lower() in seasons and seasons:
                        break
                    if not episode.lower() in episodes and episodes:
                        continue
                    if not character.lower() in characters and characters:
                        continue
                    has_text = True
                    for word in text:
                        if not word.lower() in speech.lower():
                            has_text = False
                    if has_text:
                        print(line, end="")
        except Exception as err:
            print(err, file=sys.stderr)
