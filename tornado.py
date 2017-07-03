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


        group_of_words = [adverb_word, adjective_word, article_word, noun_word, prepositions_word, verb_word]
        return group_of_words


"""

adverb = w[0]
adjective = w[1]
article = w[2]
noun = w[3]
"""

def subject_phrase(w):
    adjective = w[1]
    article = w[2]
    noun = w[3]
    phrase = []
    start = randrange(0,100)
    randnum = randrange(1,20)
    randnumonefive = randrange(1,6)
    randnumonethree = randrange(1,4)
    if start > 90:
        phrase.append(choice(words.interjections))
    if start < 10:
        phrase.append(choice(words.dont_break))

    if randnum == 1:
        # 'I', 'we', 'you', 'she', 'he', 'it', 'they'
        phrase.append(choice(words.personal_pronouns))
        # qualify himself or someone

        if randnumonefive == 1:
            phrase.append(article)
            phrase.append(noun)
        elif randnumonefive == 2:
            phrase.append(adjective) ###
            phrase.append(noun)
        elif randnumonefive == 3:
            phrase.append(article)
            phrase.append(adjective) ###
            phrase.append(noun)
        elif randnumonefive == 4:
            phrase.append(noun)    
        else:
            pass
        #print('Inside subject - randnum = {} - randnumonefive = {} : {}\n'.format(randnum, randnumonefive, phrase))
    
    elif randnum == 2:
        # 'this', 'these', 'that', 'those's
        phrase.append(choice(words.demonstrative_pronouns))
        # qualify something
        if randnumonethree == 1:
            phrase.append(noun)
        elif randnumonethree == 2:
            phrase.append(adjective)
            phrase.append(noun)
        else:
            pass
        #print('Inside subject | randnum = {} | randnumonefive = {} | {}\n'.format(randnum, randnumonefive, phrase))

    elif randnum == 3:
        # 'anybody', 'anyone', 'anything', 'each' (...)
        phrase.append(choice(words.indefinite_pronouns))

        if randrange(0,1) == 1:
            phrase.append(adverb)
        #print('Inside subject | randnum = {} | randnumonefive = {} | {}\n'.format(randnum, randnumonefive, phrase))

    elif randnum == 4:
        phrase.append(choice(words.reflexive_pronouns))
        #print('Inside subject | randnum = {} | randnumonefive = {} | {}\n'.format(randnum, randnumonefive, phrase))

    elif randnum == 5:
        phrase.append(choice(words.possessive_pronouns))
        #print('Inside subject | randnum = {} | randnumonefive = {} | {}\n'.format(randnum, randnumonefive, phrase))
        # append auxiliar be

    elif randnum == 6:
        phrase.append(choice(words.interrogative_pronouns))
        if randnumonethree == 1:
            phrase.append(choice(words.auxiliar_be))
            phrase.append(choice(words.auxiliar_be))
        elif randnumonethree == 2:
            phrase.append(choice(words.auxiliar_have))
        else:
            phrase.append(choice(words.auxiliar_do))
        #print('Inside subject | randnum = {} | randnumonefive = {} | {}\n'.format(randnum, randnumonefive, phrase))

    # No pronouns!
    elif randnum >= 10:
        if randnumonefive == 1:
            phrase.append(article)
            phrase.append(noun)
        elif randnumonefive == 2:
            phrase.append(adjective) ###
            phrase.append(noun)
        elif randnumonefive == 3:
            phrase.append(article)
            phrase.append(adjective) ###
            phrase.append(noun)
        elif randnumonefive == 4:
            phrase.append(noun)    
        else:
            pass
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
    adjective = w[1]
    article = w[2]
    noun = w[3]
    ap = []
    randnum = randrange(0,4)     
    randnumtwo = randrange(0,2)
    extent_of_action = ['very', 'too', 'almost', 'also', 'only', 'enough', 'so', 'quite', 'rather ']
    adjective = choice(words.adjectives)
    preposition = choice(words.prepositions)

    # Adjective + PP
    if randnum == 1:
        if randnumtwo == 1:
            ap.append(adjective)
            ap.append(preposition)
            ap.append(w[3])
        else:
            ap.append(adjective)
            ap.append(preposition)
            ap.append(article)
            ap.append(w[3])
        #print('Inside adjective | randnum = {} | randnumtwo = {} | {}\n'.format(randnum, randnumtwo, ap))


    elif randnum == 2:
        # Adv + A
        if randnumtwo == 1:
            ap.append(choice(extent_of_action))
            ap.append(adjective)

        # Adv + A + N
        else:
            ap.append(choice(extent_of_action))
            ap.append(adjective)
            ap.append(w[3])
        #print('Inside adjective | randnum = {} | randnumtwo = {} | {}\n'.format(randnum, randnumtwo, ap))
    
    else:
        pass

    return ap

def verb_phrase(w):
    # Helping verb + Main verb
    #    could     +   eat
    #    might     +   listen
    vp = []
    randnum = randrange(0,3)     
    #randnumtwo = randrange(0,1)
    help_verb = choice(words.modal_verbs)
    main_pr = choice(words.base)
    main_ps = choice(words.past_Simple)
    main_pp = choice(words.past_Participle)

    if randnum == 1:
        vp.append(help_verb)
        vp.append(w[5])
        #print('Inside verb | randnum = {} | {}\n'.format(randnum, vp))

    elif randnum == 2:
        vp.append(w[5])
        #print('Inside verb | randnum = {} | {}\n'.format(randnum, vp))

    else:
        pass
    return vp

def phrases(w):

        # Indepentent clause (simple)
        # <subject> <verb> <noun>
        #     1       1      1
        # Compound Sentences - made of 2 or more sentences combined using a conjunction such as and, or *or* but.
        # They are made up of more than one independent clase joined together with a coordination conjuntion.
        subject = subject_phrase(w)
        adjective = adjective_phrase(w)
        verb = verb_phrase(w)

        group_of_phrases = []
        group_of_phrases.extend(subject)
        group_of_phrases.extend(adjective)
        group_of_phrases.extend(verb)
        #group_of_phrases.extend(words.)
        print ("group_of_phrases | {} ".format(group_of_phrases))
        print('\n')
        i = len(group_of_phrases)
        a = [x for x in combinations(group_of_phrases, i)]
        line = (' '.join(choice(a)) + "\n")

        print('\n')
        #print(a)
        print ('======================================================================================')
        print('\n')
        #print('\n')
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
            sleep(0.5)




