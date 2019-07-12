# Words-Frequency
Frequency of words in files

##Code

import os

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
    Most_Frequent = dict(sorted_list[:11])

    return(Most_Frequent)


print('\nSpanish\n', frequency_table('C:\\Users\\rober\\Downloads\\cherbonnel-mi-tio_SP.txt'))
print('\nEnglish\n', frequency_table('C:\\Users\\rober\\Downloads\\eaton-boy-scouts_EN.txt'))
print('\nGerman\n', frequency_table('C:\\Users\\rober\\Downloads\\schloemp-tolle-koffer_DE.txt'))
print('\nUnknown\n', frequency_table('C:\\Users\\rober\\Downloads\\unknown-lang.txt'))

print("\nI predict this Unknown is Spanish")