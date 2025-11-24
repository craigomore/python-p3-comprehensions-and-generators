#!/usr/bin/env python3

# Task 1: Return all even numbers in the input list
def return_evens(num_list):
    # List comprehension to filter out even numbers
    return [n for n in num_list if n % 2 == 0]

# Task 2: Add an exclamation mark to each sentence in the input list
def make_exclamation(sentence_list):
    # List comprehension to add "!" to each sentence
    return [sentence + "!" for sentence in sentence_list]
