#!/usr/bin/python3
"""Script to add arguments to a Python list and save them to a JSON file."""

from sys import argv
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing data from file, or initialize an empty list
if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add the new arguments to the list
my_list.extend(argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
