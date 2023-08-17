#!/usr/bin/env python3

def return_evens(num_list):
    
   # result = []
   # for num in num_list:
    #    if(num%2== 0):
   #          result.append(num)

   # return result        


    even = [num for num in num_list if( num% 2 == 0)]   
    return even


def make_exclamation(sentence_list):
    #empty = []
    #for sentence in sentence_list:
     #   sentence1 = sentence + "!"
     #   empty.append(sentence1)

    empty1 = [sentence + "!" for sentence in sentence_list]   
    return empty1
