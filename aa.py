import sys
from itertools import combinations
from time import sleep
from random import choice, randrange, shuffle
import words
import argparse


def choosing_words():



        subject_pronouns = (words.personal_pronouns, words.demonstrative_pronouns, words.possessive_pronouns, words.indefinite_pronouns)

        articles = words.articles
        verbs = (words.base, words.past_Participle, words.past_Simple)
        adverbs = (words.adverbs_usually_before_verb, words.adverbs_of_Time)
        adjectives = (words.adjectives)
        nouns = (words.weather, words.body, words.animals, words.clothes, words.food, words.general_words, words.picturable_words, words.imaginary)


        # Choose
        # Pronoun
        subject_pronoun = choice(subject_pronouns)
        subject_pronoun_word = choice(subject_pronoun)

        # Verb
        verb = choice(verbs)
        verb_word = choice(verb)

        # Adverb
        adverb = choice(adverbs)
        adverb_word = choice(adverb)

        # Adjective
        adjective_word = choice(adjectives)

        # Article
        article_word = choice(articles)

        # Noun
        noun = choice(nouns)
        noun_word = choice(noun)

        # Preposition
        prepositions_word = choice(words.prepositions)


        group_of_words = [subject_pronoun_word, verb_word, adverb_word, adjective_word, article_word, noun_word, prepositions_word]
        return group_of_words




# The subject is the person or thing the sentence is 'about'. Often (but not always) it will be the first part of the sentence. 
# The subject will usually be a noun phrase (a noun and the words, such as adjectives, that modify it) followed by a verb.
# Types:
# Noun or pronoun - *The large car* stopped outside
# A gerund - *His constant hammering* was annoying
# A to-infinitive - *To read* is easier than to write
# A full that-clause - *That he had traved the world* was known to everyone
# A free relative clause - *Whatever he did* was always of interest
# A direct quotation - *I love you* is often heard these days
# Zero (but implied) subject - Take out the trash!
# An expletive - *It* is raining
# A cataphoric it - *It* was known by everyone that he had traveled the world


def subject(pronoun):
    phrase = []
    start = randrange(0,100)
    number = randrange(0,10)
    if start > 90:
        phrase.append(choice(words.interjections))

    if 1:
        phrase.append(choice(words.personal_pronouns))
    elif 2:
        phrase.append(choice(words.demonstrative_pronouns))
    elif 3:
        phrase.append(choice(words.indefinite_pronouns))
    elif 4:
        phrase.append(choice(words.reflexive_pronouns)) 



def phrases(w):

        # Indepentent clause (simple)
        # <subject> <verb> <noun>
        #     1       1      1
        # Compound Sentences - made of 2 or more sentences combined using a conjunction such as and, or *or* but.
        # They are made up of more than one independent clase joined together with a coordination conjuntion.
        pronoun = w[0]
        verb = w[1]
        adverb = w[2]
        adjective = w[3]
        article = w[4]
        noun = w[5]
        for i in w:
            print i
        print('article ' + article)

        if ((article == 'a') and (noun[:1] == 'a' or 'e' or 'i' or 'o' or 'u')):
            print('changing..')
            article == choice(words.articlenota)
            print('new article ' + article)
        elif ((article == 'an') and (noun[:1] != 'a' or 'e' or 'i' or 'o' or 'u')):
            print('changing..')
            article == choice(words.articlenota)
            print('new article ' + article)


        subject_pronoun = [pronoun, verb, article, noun]
        subject_noun = [article, noun, verb]

        number = randrange(0,2)
        if number == 1:
            subject_pronoun.insert(1, choice(words.adverbs_usually_before_verb))
            subject_noun.insert(2, choice(words.adverbs_usually_before_verb))

        elif number == 2:
            subject_pronoun.insert(3, adjective)
            subject_noun.insert(1, adjective)

        else:
            pass

        final = [subject_pronoun, subject_noun]



        line = (' '.join(choice(final)) + "\n").capitalize()
        return line





if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='bot for twitter')
        #parser.add_argument('-l', help='number of text lines (default 1)', type=int)
        parser.add_argument('-t', help='time for sleep in seconds (default 300)', type=int)
        args = parser.parse_args()
        t = args.t

        while True:

                filename=open('test.txt','w')
                for i in range(3):

                    filename.write(phrases(choosing_words()))
                    #phrases(choosing_words())

                filename.close()

                filename=open('test.txt','r')
                f=filename.readlines()
                filename.close()
                tweet = f[0] + f[1] + f[2]
                print (tweet)
                #api.update_status(tweet)
                sleep(300)

