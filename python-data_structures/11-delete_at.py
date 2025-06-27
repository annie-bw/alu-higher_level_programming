i#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  # Index out of range; return list unchanged

    del my_list[idx]  # Delete the item at the given index
    return my_list
