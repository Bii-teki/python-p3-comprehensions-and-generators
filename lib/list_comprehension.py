#!/usr/bin/env python3

def return_evens(num_list):
    
   
    even = [num for num in num_list if( num% 2 == 0)]   
    return even


def make_exclamation(sentence_list):
    empty = []
    for sentence in sentence_list:
        sentence1 = sentence + "!"
        empty.append(sentence1)
    return empty
