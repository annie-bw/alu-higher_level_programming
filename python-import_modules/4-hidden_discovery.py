#!/usr/bin/env python3

if __name__ == "__main__":
    import importlib.util
    import sys

    module_name = "hidden_4"
    file_path = "./hidden_4.pyc"

    # Load the compiled module from file
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Filter and sort the attributes
    names = sorted(name for name in dir(hidden_4) if not name.startswith("__"))

    # Print each name
    for name in names:
        print(name)
