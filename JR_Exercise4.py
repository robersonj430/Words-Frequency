# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:06:44 2019

@author: rober
"""

Unknown_Files = {'Unknown 1':'unknown-lang.txt', 'Unknown 2':'Unknown-100000.txt',
                 'Unknown 3':'Unknown-pg23620.txt', 'Unknown 4':'Unknown-pg6110.txt'}
Training_Files = {'Spanish':'cherbonnel-mi-tio_SP.txt','English':'eaton-boy-scouts_EN.txt',
         'German':'schloemp-tolle-koffer_DE.txt','Portugese':'15047-0_PE.txt'}

import os
os.chdir("C:\\Users\\rober\\OneDrive\\Desktop\\IMT511\\Words-Frequency")

def frequency_table(file_name):
    with open(file_name, encoding='utf-8') as f:
        content = f.read()
    content_strip = content.strip("|©!@#$%^&*()-_=+,.;:?/<>'`[]")
    Word_List = content_strip.split()
    total_words = len(Word_List)
    frequency = {}
    for w in Word_List:
        if len(w)>5:
            continue
        if w not in frequency:
            frequency[w] = 0
        frequency[w] += 1
    for w in frequency:
        frequency[w] = frequency[w]/total_words
    sorted_list = sorted(frequency.items(), key=lambda kv: kv[1], reverse=True)
    Most_Frequent = dict(sorted_list[:21])
    return(Most_Frequent)

frequency_training_dict = {}
for f in Training_Files:
    frequency_language = frequency_table(Training_Files[f])
    frequency_training_dict.update({f:frequency_language})
    
frequency_unknown_dict = {}
for f in Unknown_Files:
    frequency_language = frequency_table(Unknown_Files[f])
    frequency_unknown_dict.update({f:frequency_language})

def Summation(dict1, dict2):
    language_sum = 0.0
    for w in dict1.keys():
        language_sum += abs(dict1[w] - dict2.get(w,0))
    return language_sum

print('\n')
for uk in frequency_unknown_dict:
    distance_dict = {}
    for k in frequency_training_dict:
        diff = Summation(frequency_unknown_dict[uk], frequency_training_dict[k])
        distance_dict.update({k:diff})
        distance_dict_sorted = sorted(distance_dict.items(), key=lambda kv: kv[1])
    
    print("File:"+ "'"+uk+"'", "is probably", distance_dict_sorted[0][0]+'!')


