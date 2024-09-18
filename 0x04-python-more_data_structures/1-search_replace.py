#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''Replaces all occurrences of an element by another in a new liist'''
    new_liist = my_list[:]
    for index in range(len(new_liist)):
        if new_liist[index] == search:
            new_liist[index] = replace
    return (new_liist)
