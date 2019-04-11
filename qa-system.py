# -*- coding: utf-8 -*-
#######################################################################################################################################
#######################################################################################################################################
#####
##### Brandon Chin
##### Tuesday, February 5th, 2019
##### CMSC 416 - Natural Language Processing
##### Programming Assignment 1 - Eliza Chatbot
#####
##### 1. The Problem
##### This program is a simulation of the Eliza chatbot which engages ina a dialogue with the user.
##### The program acts as a psychotherapist using "word spotting" and recognizing key words in order to respond.
##### The program is also able to transform simple statements into questions that the program asks the user.
##### The program also personalizes the dialogue by asking for the user's name, and your responses will have your name in []
##### This program relies on regular expressions in order to decipher the user's input and make a response
#####
##### 2. Example Input/Output
#####
##### [Eliza]: Hi. What is your name?
##### [User]: Brandon
##### [Eliza]: Hello Brandon! My name is Eliza, how can I help you?
##### [Brandon]: I want to cry
##### [Eliza]: Why do you want to cry?
##### [Brandon]: Because I need to cry
##### [Eliza]: Why do you need to cry?
##### [Brandon]: Because I crave happiness
##### [Eliza]: Why are you craving happiness?
##### [Brandon]: Because I am always sad
##### [Eliza]: Can you think of a specific example?
##### [Brandon]: When I was made to cry
##### [Eliza]: Why were you made to?
##### [Brandon]: Because my friend is mean all the time
##### [Eliza]: In what way?
##### [Brandon]: Like when I gave the money to charity
##### [Eliza]: Why would you give charity money?
##### [Brandon]: Because I am a good person
##### [Eliza]: Why are you a good person?
##### [Brandon]: because I try to be happy
##### [Eliza]: Can you provide an example of that?
##### [Brandon]: Nevermind, goodbye
##### [Eliza]: Take care.
#####
##### 3. Algorithm
#####
##### #1. Greet the user and get their name for continued use
#####
##### #2. Keywords and predetermined phrases based on keywords are set
#####
##### #3. Create loop, that will loop continue infinitely unless exit condition is taken. If program does not know what you say,
##### it respondds with a default response. The only time it exits is if you tell it to exit
#####
##### #4. Several foreach loops to check the statements for my keywords phrases and output a randomly reponse. In some cases,
##### the statement is transformed into a question and asked without having to check the keyword array
#####
##### #5. There is a match variable to prevent double responses which is used with the foreach loops. The other parts do not need
##### this check, as their response takes priority over the other loops
#####
##### #6. User at any time can use an exit word, and the program will end with Eliza printing an exit response
#####
#######################################################################################################################################
#######################################################################################################################################

import re
import sys
from decimal import Decimal
from random import *
import operator
from string import punctuation
import nltk
import wikipediaapi
from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize
from nltk import PorterStemmer
import lxml.html
import string

def main():##main method

    print("This is a QA system by Brandon Chin. It will try to answer questions that start with Who, What, When or Where. Enter 'exit' to leave the program.")


    while (1):

        questionInput = input("");
        print ("Your input is: ", questionInput)

        questionInput = ''.join([letter for letter in questionInput if letter not in punctuation])

        print ("Your input after punc removal is: ", questionInput)

        questionPhraseTokens = []
        queryPhraseTokens = []


        if (questionInput == "exit"):
            break
        sentenceTokens = generate_Tokens(questionInput)

        posTokens = nltk.pos_tag(sentenceTokens)

        answerType = None
        tokenIndex = 0

        if posTokens[tokenIndex][0] == "What":
            answerType = "definition"

        if posTokens[tokenIndex][0] == "Who":
            answerType = "person"

        if posTokens[tokenIndex][0] == "When":
            answerType = "date"

        if posTokens[tokenIndex][0] == "Where":
            answerType == "location"

        tokenIndex += 1
        if posTokens[tokenIndex][1] == "VBZ":
            queryPhraseTokens.append(posTokens[tokenIndex][0])
        tokenIndex += 1

        if posTokens[tokenIndex][1] == "NNP":
            stillNounPhrase = True
            while(stillNounPhrase == True):
                if tokenIndex >= len(posTokens):
                    stillNounPhrase = False
                else:
                    questionPhraseTokens.append(posTokens[tokenIndex][0])

                tokenIndex += 1

        # if posTokens[tokenIndex][1] == "NN":
        #     stillNounPhrase = True
        #     while(stillNounPhrase == True):
        #         if tokenIndex >= len(posTokens):
        #             stillNounPhrase = False
        #         else:
        #             questionPhraseTokens.append(posTokens[tokenIndex][0])
        #         tokenIndex += 1


        wiki_Search(questionPhraseTokens, queryPhraseTokens, None, None)
        # print("pos is: " + str(posTokens))

def generate_Tokens(s):

    # Replace new lines with spaces
    s = re.sub(r'\s+', ' ', s)

    # s = re.sub(r')

    # Break sentence into the tokens, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]

    print("tokens: " + str(tokens))

    return tokens

    # for i in range(len(tokens)):
        # print "Tokens {}: {}".format(i+1, tokens[i])
        # currToken = tokens[i]


wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

p_wiki=wiki_wiki.page("Test 1")
print(p_wiki.text)

wiki_html=wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.HTML
)

def wiki_Search(questionPhraseTokens, queryPhraseTokens, answerTypes, answerPattern):

    questionPhrase = ""
    queryPhrase = ""
    # questionPhrase = "George Washington"
    # questionPhraseTokens = word_tokenize(questionPhrase)
    # queryPhrase = "born"
    # queryPhraseTokens = word_tokenize(queryPhrase)
    # answerTypes = ["NNP", "CD"]
    # answerPattern = ["NNP", "CD", "CD"]

    # questionPhrase = "Abraham Lincoln"
    # questionPhraseTokens = word_tokenize(questionPhrase)
    # queryPhrase = "die"
    # queryPhraseTokens = word_tokenize(queryPhrase)
    # answerTypes = ["NNP", "CD"]
    # answerPattern = ["NNP", "CD", "CD"]

    # questionPhrase = "Pennsylvania"
    # questionPhraseTokens = word_tokenize(questionPhrase)
    # queryPhrase = "capital"
    # queryPhraseTokens = word_tokenize(queryPhrase)
    # answerTypes = ["NNP"]
    # answerPattern = ["NNP"]

    # questionPhrase = "Virginia"
    # questionPhraseTokens = word_tokenize(questionPhrase)
    # queryPhrase = "largest city"
    # queryPhraseTokens = word_tokenize(queryPhrase)
    # answerTypes = ["NNP"]
    # answerPattern = ["NNP"]

    # questionPhrase = "Oregon"
    # questionPhraseTokens = word_tokenize(questionPhrase)
    # queryPhrase = "largest city"
    # queryPhraseTokens = word_tokenize(queryPhrase)
    # answerTypes = ["NNP"]
    # answerPattern = ["NNP"]

    # questionPhrase = "Virginia"
    # questionPhraseTokens = word_tokenize(questionPhrase)
    # queryPhrase = "total area"
    # queryPhraseTokens = word_tokenize(queryPhrase)
    # answerTypes = ["CD", "JJ", "NNS"]
    # answerPattern = ["CD", "JJ", "NNS"]
    #

    print("questionPhraseTokens " + str(questionPhraseTokens))

    questionPhrase = string.join(questionPhraseTokens)

    queryPhrase = string.join(queryPhraseTokens)


    print("Asking about " + questionPhrase + " " + queryPhrase)
    print("subject tokens: ")
    print(questionPhraseTokens)
    print("question tokens: ")
    print(queryPhraseTokens)

    p_html=wiki_html.page(questionPhrase)
    print(p_html.text)

    #print("Categories")
    #print_categories(p_html)

    #print("Sections")
    #print_sections(p_html.sections)

    page = lxml.html.document_fromstring(p_html.text)
    wikitextonly = page.cssselect('body')[0].text_content()

    #print(wikitextonly)

    sentences = sent_tokenize(wikitextonly)
    sentenceIndex = 0
    answerFound = False
    interestingSentences = dict()

    while answerFound == False and sentenceIndex < len(sentences):
        currentSentence = sentences[sentenceIndex]
        #print("Sentence " + str(sentenceIndex))
        #print(sentences[sentenceIndex])

        # break into tokens
        sentenceTokens = word_tokenize(currentSentence)

        # remove punctuation
        table = str.maketrans('', '', string.punctuation)
        stripped = [words.translate(table) for words in sentenceTokens]

        # remove non-alphabetic tokens
        alphabeticTokens = [word for word in stripped if (word.isalpha() or word.isnumeric())]
        #alphabeticTokens = stripped

        # filter out stop words
        stopWords = set(stopwords.words('english'))
        sanitizedWords = [word for word in alphabeticTokens if not word in stopWords]
        stemmer = PorterStemmer()

        # sanitize the sentence
        #print("Sanitized: ")
        #print(sanitizedWords)

        posTaggedWords = (nltk.pos_tag(sanitizedWords))

        #print(posTaggedWords)

        # find something interesting if NNP matches tokens
        interestLevel = 0

        # first look through subject tokens for match in sentence
        for aSubjectToken in questionPhraseTokens:
            for posTaggedWord, pos in posTaggedWords:
                if posTaggedWord == aSubjectToken:
                    #print("SubjectToken " + aSubjectToken + " matches")
                    # look for part of speech match on NNP
                    if pos == "NN" or pos == "NNP":
                        interestLevel += 1
                        if pos == "NNP":
                            # extra bonus for being a proper noun
                            #print("POS tag also matches")
                            interestLevel += 1
                        break # to stop further matching on same subjectToken

        for aQuestionToken in queryPhraseTokens:
            for posTaggedWord, pos in posTaggedWords:
                # stem for the question tokens, we want a meaning match here, while
                # questionPhraseTokens we want to be exact match
                if stemmer.stem(aQuestionToken) == stemmer.stem(posTaggedWord):
                    #print("QuestionToken " + aQuestionToken + " matches")
                    interestLevel += 1
                    if pos == "NN":
                        # question is a NN, more likely to be the right one
                        interestLevel += 1
                    break

        # look the right type of answers
        for posTaggedWord, pos in posTaggedWords:
            if pos in answerTypes:
                interestLevel += 1
                break # to stop further matching on same answerType


        # for currentWord, posTag in posTaggedWords:
        #     if( currentWord in questionPhraseTokens):
        #         print("currentWord: " + currentWord + " matches subjectToken(s)")
        #         if( posTag == "NNP"):
        #             print("posTag also matches")
        #             interestLevel += 1
        #     if( currentWord in queryPhraseTokens):
        #         print("currentWord: " + currentWord + " matches questionToken(s)")
        #         interestLevel += 1


        # if sentence is interesting
        if interestLevel > 1:
            print("interesting sentence at level " + str(interestLevel))
            print(currentSentence)
            print(posTaggedWords)
            interestingSentences[currentSentence] = [interestLevel, posTaggedWords]
            print("----")

        sentenceIndex += 1


    print("interesting sentences")
    highestInterestLevel = 0
    mostInterestingSentence = None
    mostInterestingTaggedWords = None

    for sentence, items in interestingSentences.items():
        #print( "sentence: " + str(sentence) )
        #print( "interest level " + str(interestLevel))
        interestLevel = items[0]
        posTaggedWords = items[1]
        if interestLevel > highestInterestLevel:
            highestInterestLevel = interestLevel
            mostInterestingSentence = sentence
            mostInterestingTaggedWords = posTaggedWords

    if mostInterestingSentence == None:
        print("I am not sure, please ask in a different way")
    else:
        print(mostInterestingSentence)
        print("interest level: " + str(highestInterestLevel))
        print(mostInterestingTaggedWords)

    answerNoQuestionPhraseWords = [word for word in mostInterestingTaggedWords if not word[0] in questionPhraseTokens]
    answerPhraseWords = [word for word in answerNoQuestionPhraseWords if not stemmer.stem(word[0]) in queryPhraseTokens]

    answerTokens = []

    for answerCandidate in answerPhraseWords:
        if answerCandidate[1] in answerTypes:
            answerTokens.append(answerCandidate)
    print( "answer tokens: ")
    print( answerTokens)


    # answer pattern match
    answerPatternIndex = 0
    stillMatch = False
    fullMatch = False

    answerWords = []

    if len(answerPattern) == 0:
        answerWords = answerTokens
    else:
        for aToken in answerTokens:
            #print("answerpattern index " + str(answerPatternIndex))
            if aToken[1] == answerPattern[answerPatternIndex]:
                #print("matched token with pattern " + aToken[0])
                stillMatch = True
                answerWords.append(aToken[0])
                answerPatternIndex += 1
            else:
                stillMatch = False
                answerWords = []
                answerPatternIndex = 0

                # check to see if pattern starts over
                if aToken[1] == answerPattern[answerPatternIndex]:
                    stillMath = True
                    answerWords.append(aToken[0])
                    answerPatternIndex += 1

            if stillMatch == True:
                if answerPatternIndex >= len(answerPattern):
                    # we have a full match
                    fullMatch = True
                    break

        if fullMatch == True:
            #print("full match with ")
            print(answerWords)


if __name__ == "__main__":
    main()
