import sys
from itertools import combinations
from time import sleep
from random import choice, randrange, shuffle
import words
import argparse


def choosing_words():

        # Take from dictionary

        verbs = (words.base, words.past_Participle, words.past_Simple)

        adverbs = (words.adverbs_usually_before_verb, words.adverbs_of_Time)

        nouns = (words.weather, words.body, words.animals, words.clothes, words.general_words, words.picturable_words, words.imaginary, words.qualities)


        # Choose


        # Verb
        verb = choice(verbs)
        verb_word = choice(verb)
        # Adverb
        adverb = choice(adverbs)
        adverb_word = choice(adverb)
        # Noun
        noun = choice(nouns)
        noun_word = choice(noun)
        #weather
        wheather_word = choice(words.weather)
        #ly
        ly_word = choice(words.ly)
        #prepositions
        prepositions_word = choice(words.prepositions)
        #descriptive_words
        descriptive = choice(words.descriptive_words)
        poss = choice(words.poss)
        group_of_words = [verb_word, adverb_word, noun_word, wheather_word, ly_word, descriptive, poss, prepositions_word]
        return group_of_words

def phrases(group_of_words):
        shuffle(group_of_words)
        i = randrange(1,5)
        results = [x for x in combinations(group_of_words, i) ]
        results = choice(results)
        ##print(results)
        #print("\n")
        #print("results: \n")
        #print(results)
        line = (' '.join(results) + "\n").capitalize()
        return line

if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Shit poster bot for twitter')
        #parser.add_argument('-l', help='number of text lines (default 1)', type=int)
        parser.add_argument('-t', help='time for sleep in seconds (default 300)', type=int)
        args = parser.parse_args()
        t = args.t

        while True:

                filename=open('test.txt','w')
                for i in range(3):

                    filename.write(phrases(choosing_words()))

                filename.close()

                filename=open('test.txt','r')
                f=filename.readlines()
                filename.close()
                tweet = f[0] + f[1] + f[2]
                print (tweet)
                #api.update_status(tweet)

