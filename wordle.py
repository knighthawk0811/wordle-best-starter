#!/usr/bin/env python3

'''
J Neathawk
Best Wordle Starting Words

Find the frequency of each letter position 1-5
Then read the chart and make some words
'''

#create a list of letters, this will be helpful later
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#read the word list
with open('wordle-list.txt') as file:
    data = [word.split('\n')[0] for word in file.readlines()]
    
#find the frequency of each letter in each slot
frequency = [[0] * 26 for x in range(5)]
for word in data:
    for index, character in enumerate(word):
        frequency[index][ord(character) - 97] += 1

#find the overall frequency of each letter
frequency_overall = [0]*26
for i in range(5):
    for j in range(26):
        frequency_overall[j] += frequency[i][j]

#find most popular letters overall
previous = 2000
temp = 0
popular_letters = [None]*26
for i in range(26):
    for j in range(26):
        if( frequency_overall[j] > temp and frequency_overall[j] < previous):
            temp = frequency_overall[j]
            popular_letters[i] = letters[j]
    previous = temp
    temp = 0


#find the top 5 letters in each slot
previous = 2000
temp = 0
top_characters = [0]*5
for i in range(5):
    top_characters[i] = [None]*26
    
    for j in range(26):
        for k in range(26):
            if( frequency[i][k] > temp and frequency[i][k] <= previous):
                if letters[k] not in top_characters[i]:
                    temp = frequency[i][k]
                    top_characters[i][j] = letters[k]
        previous = temp                
        temp = 0
        
    previous = 2000                
    temp = 0

#print
print()
print( popular_letters )

#print the frequency of each slot
print()
for j in range(26):
    print( '{} | {:4d} - {:4d} - {:4d} - {:4d} - {:4d} | {:4d} '.format(letters[j], frequency[0][j], frequency[1][j], frequency[2][j], frequency[3][j], frequency[4][j], frequency_overall[j]))


#print best in slot
print()
for j in range(9):
    print( '{} | {} | {} | {} | {} '.format(top_characters[0][j], top_characters[1][j], top_characters[2][j], top_characters[3][j], top_characters[4][j]))
    print('-----------------')


#breakpoint = 0
