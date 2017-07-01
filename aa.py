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


def subject_phrase(w):
    phrase = []
    start = randrange(0,100)
    randnum = randrange(1,7)
    randnumtwo = randrange(1,10)
    if start > 90:
        phrase.append(choice(words.interjections))
    if start < 10:
        phrase.append(choice(words.dont_break))

    if randnum == 1:
        phrase.append(choice(words.personal_pronouns))
        # qualify himself or someone

        if randnumtwo == 1:
            phrase.append(w[4])
            phrase.append(w[5])
        elif randnumtwo == 2:
            phrase.append(w[3])
            phrase.append(w[5])
        elif randnumtwo == 3:
            phrase.append(w[4])
            phrase.append(w[3])
            phrase.append(w[5])
        elif randnumtwo == 4:
            phrase.append(w[5])    
        else:
            pass
    

    elif randnum == 2:
        # 'this', 'these', 'that', 'those's
        phrase.append(choice(words.demonstrative_pronouns))
        # qualify something
        if randnumtwo == 1:
            phrase.append(w[5])
        elif randnumtwo == 2:
            phrase.append(w[3])
            phrase.append(w[5])
        else:
            pass


    elif randnum == 3:
        # 'anybody', 'anyone', 'anything', 'each' (...)
        phrase.append(choice(words.indefinite_pronouns))

        if randnumtwo == 2:
            phrase.append(adverb)

    elif randnum == 4:
        phrase.append(choice(words.reflexive_pronouns))
    elif randnum == 5:
        phrase.append(choice(words.possessive_pronouns))
        # append auxiliar be
    elif randnum == 6:
        phrase.append(choice(words.interrogative_pronouns))
        if randnumtwo == 1:
            phrase.append(choice(words.auxiliar_be))
            phrase.append(choice(words.auxiliar_be))
        elif randnumtwo == 2:
            phrase.append(choice(words.auxiliar_have))
        if randnumtwo == 3:
            phrase.append(choice(words.do))
    else:
        pass


    # Continue 
    #print phrase
    return phrase
    #call_for_verb_function(subject_phrase)


def adjective_phrase(w):
    #  Adj + PP -> P + N  Angry with.you
    #  A + P + M 
    #  Adv + A  Too happy
    ap = []
    randnum = randrange(0,2)     
    randnumtwo = randrange(0,1)
    extent_of_action = ['Very', 'Too', 'Almost', 'Also', 'Only', 'Enough', 'So', 'Quite', 'Almost', 'Rather ']
    adjective = choice(words.adjectives)
    preposition = choice(words.prepositions)

    # Adjective + PP
    if randnum == 1:
        if randnumtwo == 1:
            ap.append(adjective)
            ap.append(preposition)
            ap.append(w[5])
        else:
            ap.append(adjective)
            ap.append(preposition)
            ap.append(w[4])
            ap.append(w[5])


    elif randnum == 2:
        # Adv + A
        if randnumtwo == 1:
            ap.append(extent_of_action)
            ap.append(adjective)

        # Adv + A + N
        else:
            ap.append(extent_of_action)
            ap.append(adjective)
            ap.append(w[5])
    else:
        pass

    return ap

def verb_phrase(w):
    # Helping verb + Main verb
    #    could     +   eat
    #    might     +   listen
    vp = []
    randnum = randrange(0,2)     
    randnumtwo = randrange(0,1)
    help_verb = choice(words.modal_verbs)
    main_pr = choice(words.base)
    main_ps = choice(words.past_Simple)
    main_pp = choice(words.past_Participle)

    if randnum == 1:
        vp.append(help_verb)
        vp.append(w[1])

    elif randnum == 2:
        vp.append(w[1])

    else:
        pass
    return vp




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
        subject = subject_phrase(w)
        adjective = adjective_phrase(w)
        verb = verb_phrase(w)
        print(subject)
        print(adjective)
        print(verb)
        print('\n')

        line = (' '.join(final) + "\n").capitalize()
        return line
"""

        if ((article == 'a') and (noun[:1] == 'a' or 'e' or 'i' or 'o' or 'u')):
            print('changing..')
            article == choice(words.articlenota)
            print('new article ' + article)
        elif ((article == 'an') and (noun[:1] != 'a' or 'e' or 'i' or 'o' or 'u')):
            print('changing..')
            article == choice(words.articlenota)
            print('new article ' + article)
"""




if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='bot for twitter')
        #parser.add_argument('-l', help='number of text lines (default 1)', type=int)
        parser.add_argument('-t', help='time for sleep in seconds (default 300)', type=int)
        args = parser.parse_args()
        t = args.t

        phrases(choosing_words())

