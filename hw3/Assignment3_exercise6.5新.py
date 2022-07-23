text = ('This is sample text with several words '
'this is more sample text with some different words')
word_counts = {}
textcap = text.upper() #ignore upper and lower case
# count occurrences of each unique word
for word in textcap.split():
    if word in word_counts:
        word_counts[word] += 1  #increment count 
    else:
        word_counts[word] = 1

print(f'{"WORD":<18} COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<20}{count}')

    print('\nNumber of unique words: ',len(word_counts) )


    print("Duplicate words: ")
for word, count in word_counts.items():
    if word_counts[word] > 1:
        print(f'{word:<20}')
