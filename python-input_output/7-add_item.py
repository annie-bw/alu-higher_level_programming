#!/usr/bin/python3
"""Adds all arguments to a list and saves them to add_item.json"""

import sys
import os

if __name__ == "__main__":
    from importlib import import_module

    # Import the required functions
    save_to_json_file = import_module("5-save_to_json_file").save_to_json_file
    load_from_json_file = import_module("6-load_from_json_file").load_from_json_file

    filename = "add_item.json"

    # Load existing list or create a new one
    data = load_from_json_file(filename) if os.path.exists(filename) else []

    # Add command-line arguments (excluding the script name)
    data += sys.argv[1:]

    # Save updated list
    save_to_json_file(data, filename)
