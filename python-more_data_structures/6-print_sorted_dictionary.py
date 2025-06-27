#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    
    # Simple bubble sort to sort the keys alphabetically (since we can't use sorted())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if keys[i] > keys[j]:
                keys[i], keys[j] = keys[j], keys[i]
    
    for key in keys:
        print(f"{key}: {a_dictionary[key]}")
