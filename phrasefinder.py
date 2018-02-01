"""
Finds phrases inside of a text document

"""

#Imports
import os
import sys
import string
import nltk
from nltk.tokenize import RegexpTokenizer

# Script info
__author__ = "Mike Davies"

def find_phrases(document):
    """
    logic flow:
    get sentences
    get words in sentences
    build possible phrases - 3 to 10 words long
    add phrases to new phrase list, increment if already exists
    remove phrases that do not repeat
    remove subphrases
    get the 10 most frequent phrases
    """

    # get the class to help us out
    nltk.download('punkt')

    # extract sentences from the document
    print("Extracting Sentences")
    sentences = nltk.sent_tokenize(document)
    totalsentences = len(sentences)
    print(str(totalsentences) + " sentences in document")

    sentencecount=0
    # create an empty dictionary
    phrases = {}

    # loop through each sentence
    for sentence in sentences:
        sentencecount += 1
        print("analyzing sentence " + str(sentencecount) + " of " + str(totalsentences))

        # extract the words in the sentence
        words = nltk.word_tokenize(sentence)

        totalwords = len(words)

        # loop through each word to build phrases. ignore the last couple words since they make too small phrases
        for x in range(0, totalwords - 2):

            # Don't start with punctuation
            if words[x] not in string.punctuation:

                # start building up to next 10 words
                i = 0
                phrase = ""
                for y in range(0, 10):

                    # only continue while we are not out of bounds
                    while x+i < len(words):

                        # increment past punctuation, don't count it as a word
                        if words[x+i] in string.punctuation:
                            i += 1
                            continue

                        # add the current word to the phrase
                        phrase = phrase + words[x+i] + " "

                        # if it is a 3 or more word phrase, log it!
                        if y >= 2:

                            # lower case and trim it to save the phrase
                            savephrase = phrase.lower().strip()
                            # if the phrase is already in our dictionary, then increment value
                            if savephrase in phrases:
                                phrases[savephrase] = phrases[savephrase] + 1
                            else:
                                phrases[savephrase] = 1

                        i += 1
                        break

    # remove anything with a count of 1, use a list cause otherwise it errs resizing while looping
    for phrase in list(phrases):
        if phrases[phrase] == 1:
            phrases.pop(phrase)
    # remove subphrases (this is totally not optimal!)
    for subphrase in list(phrases):
        for superphrase in list(phrases):
            if subphrase != superphrase and subphrase in superphrase:
                phrases.pop(subphrase)
                break

    # echo the phrase count
    print(str(len(phrases)) + " total phrases")

    # sort the dictionary
    sorteddict = sorted(phrases.items(), key=lambda kv: kv[1], reverse=True)

    # get the top 10 (or tied for top 10)!!
    tenval = sorteddict[9][1]
    for phrase in sorteddict:
        if phrase[1] < tenval:
            break
        print(phrase)

# read the sample, execute the function!
file = open("sample.txt", "r")
find_phrases(file.read())
