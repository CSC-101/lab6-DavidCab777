from dataclasses import replace

import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
def selection_sort_books(values:list[data.Book]):
    for idx in range(len(values) - 1):
        mindex = from_smallest_book(values,idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] =  tmp

def from_smallest_book(values:list[""], start:int):
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex
# Part 2
def swap_case(words:str):
    new = [] #creates list to add the swapped letters
    for i in words:
        if i.isupper():
            new.append(i.lower())
        elif i.islower:
            new.append(i.upper())

    new = ''.join(new) #fixes the list to return type str
    return new

# Part 3
def str_translate(string:str, old:str, new:str):
    string2 = [] #creates list to add the new string with the old letters swapped to new ones
    for i in string:
        if i == old: #will run if the letter needs to be replaced
            string2.append(new)
        elif i != old: #if not needed to be replaced it will append same letter
            string2.append(i)

    string2 = ''.join(string2) #returns list
    return string2


# Part 4
def histogram(string:str):
    count = {} #start dictionary
    string = string.split()
    for i in string:
        if i.isalpha(): #checks if alphabet
            if i not in count:
                count[i] = 1 #first adds to the dictionary
            else:
                count[i] += 1 #adds count to the existing key

    return count #returns dictionary