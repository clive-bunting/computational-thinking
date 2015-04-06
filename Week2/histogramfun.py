import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def proportionVowels(word):
    vowels = 0
    for c in word:
        if c.upper() == 'A' or c.upper() == 'E' or c.upper() == 'I' or c.upper() == 'O' or c.upper() == 'U':
            vowels += 1
    proportion = float(vowels) / float(len(word))
    return proportion

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    props = []
    for word in wordList:
        props.append(proportionVowels(word))
    pylab.hist(props, bins = 21)    
    pylab.show()
    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
