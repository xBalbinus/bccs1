''''
The following question is about words in the Scrabble dictionary word list.

Write a program that reads an integer from input, call this n, and does the following for the corresponding value of n:

n=1 Print the length of the longest word.
n=2 Print the first ten 15-letter words to appear in the word list. Only print one word per line.
n=3 Prints all words with at least 5 occurrences of 'a'. Use the built in function count. Only print one word per line.
ex. "bananas".count('a') is 3
n=4 Prints all the words with the maximum possible number of occurrences of 'e'.
For instance, if you determine that the Scrabble word with the most occurrences of 'e' has 5 occurrences of 'e', then your code should print each word in the Scrabble word list with 5 occurrences of 'e', one word per line.
n=5 Print all palindromes of the longest possible length. Only print one word per line.
Palindromes are words that are the same backwards as forwards (ex. 'racecar').
For instance, if you determine that the longest palindrome in the Scrabble dictionary has 6 letters, then your code should print all palindromes of length 6.
n=6 Print all words that contain the letter 'q' but do not contain the string 'qu'. Only print one word per line.

'''

def getwordlist():
    f = open('../twl06.txt')
    return [t[:-1] for t in f]

wordlist = getwordlist()

n = int(input())

def main(n):
    if n == 1:
        longestword = wordlist[0]
        for i in wordlist:
            if (len(i) > len(longestword)):
                longestword = i
        return(longestword)
    elif n == 2:
        wordcounter = 0
        for i in wordlist:
            if len(i) == 15 and wordcounter <= 9:
                print(i)
                wordcounter += 1
    elif n == 3:
        for i in wordlist:
            if i.count("a") >= 5:
                print(i)
    elif n == 4:
        max_e_count = 0
        for i in wordlist:
            if i.count("e") > max_e_count:
                max_e_count = i.count("e")
        for j in wordlist:
            if j.count("e") == max_e_count:
                print(j)
    elif n == 5:
        length_palindrome = 0
        for i in wordlist:
            ispalindrome = 1
            for k in range(len(i)-1):
                if i[k] != i[(len(i)-1-k)]:
                    ispalindrome = 0
            if ispalindrome == 1 and len(i) >= length_palindrome:
                length_palindrome = len(i)
        for j in wordlist:
            ispalindrome = 1
            for l in range(len(j)-1):
                if j[l] != j[(len(j)-1-l)]:
                    ispalindrome = 0
            if ispalindrome == 1 and len(j) == length_palindrome:
                print(j)
    elif n == 6:
        for i in wordlist:
            if (i.count("q") != 0) and (i.count("qu") == 0):
                print(i)
    
main(n)