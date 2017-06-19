import  time, sys
import random, itertools
import words
import argparse


verb_word = 0
adverb_word = 0
noun_word = 0
wheather_word = 0
ly_word = 0
prepositions_word = 0
descriptive = 0
poss = 0
line = 0

def choosing_words():

	global verb_word
	global adverb_word
	global noun_word
	global wheather_word
        global ly_word
	global prepositions_word
	global descriptive
        global poss	
	
        # Take from dictionary

	verbs = (words.base, words.past_Participle, words.past_Simple)
	
        adverbs = (words.adverbs_usually_before_verb, words.adverbs_of_Time)
	
        nouns = (words.weather, words.body, words.animals, words.clothes, words.general_words, words.picturable_words, words.imaginary, words.qualities)

	
	# Choose


	# Verb
	verb = random.choice(verbs)
	verb_word = random.choice(verb)
	# Adverb
	adverb = random.choice(adverbs)
	adverb_word = random.choice(adverb)
	# Noun
	noun = random.choice(nouns)
	noun_word = random.choice(noun)
	#weather
	wheather_word = random.choice(words.weather)
	#ly
	ly_word = random.choice(words.ly)
	#prepositions
	prepositions_word = random.choice(words.prepositions)
	#descriptive_words
	descriptive = random.choice(words.descriptive_words)
        poss = random.choice(words.poss)



def phrases():
	
	##global line

	group_of_words = [verb_word, adverb_word, noun_word, wheather_word, ly_word, descriptive, poss, prepositions_word]
	random.shuffle(group_of_words)
	i = random.randrange(1,5)
	results = [x for x in itertools.combinations(group_of_words, i) ]
	random_results = random.choice(results)
	##print(results)
	#print("\n")
	#print("random_results: \n")
	#print(random_results)
        line = (' '.join(random_results) + "\n").capitalize()
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

			#pick the words
			choosing_words()
			#make the sentences
			#print('adding to file: ' + line)
			filename.write(phrases())
			
		filename.close()		
		
		filename=open('test.txt','r')
		f=filename.readlines()
		filename.close()
		tweet = f[0] + f[1] + f[2]
		print (tweet)
		#api.update_status(tweet)

		time.sleep(t)

	
	




 





