''''
Write a program that reads a string from input, 
call this word, 
and prints each anagram of word found in the list Scrabble dictionary.
'''

def getwordlist():
    f = open('../twl06.txt')
    return [t[:-1] for t in f]

wordlist = getwordlist()

word = input()

def scrabblecheater(word):
    for i in wordlist:
        possible_anagram = ''.join(sorted(i))
        if possible_anagram == ''.join(sorted(word)):
            print(i)
            
scrabblecheater(word)