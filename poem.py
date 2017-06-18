import  time, sys
import random, itertools
import words



verb_word = 0
adverb_word = 0
things_word = 0
wheather_word = 0
ly_word = 0
prepositions_word = 0
descriptive_words = 0
line = 0

def choosing_words():

	global verb_word
	global adverb_word
	global things_word
	global wheather_word
	global ly_word
	global prepositions_word
	global descriptive
	
	#######GROUP
	verbs = (words.base, words.past_Participle, words.past_Simple)
	adverbs = (words.adverbs_usually_before_verb, words.adverbs_of_Time)
	#adverbs = (words.adverbs_of_Quantity, words.adverbs_of_Cause, words.adverbs_of_Place, words.adverbs_of_Time)
	things = (words.body, words.animals, words.clothes, words.general_words, words.picturable_words, words.imaginary, words.qualities)

	
	#######CHOOSE
	#verb
	verb = random.choice(verbs)
	verb_word = random.choice(verb)
	#adverb
	adverb = random.choice(adverbs)
	adverb_word = random.choice(adverb)
	#things
	thing = random.choice(things)
	things_word = random.choice(thing)
	#weather
	wheather_word = random.choice(words.weather)
	#ly
	ly_word = random.choice(words.ly)
	#prepositions
	#prepositions_word = random.choice(words.prepositions)
	#descriptive_words
	descriptive = random.choice(words.descriptive_words)


def printing():
	
	stuff_to_print = [verb_word, adverb_word, things_word, wheather_word, ly_word, descriptive]
	for stuff in stuff_to_print:
		print(stuff)


def phrases():
	
	global line

	group_of_words = [verb_word, adverb_word, things_word, wheather_word, ly_word, descriptive]
	random.shuffle(group_of_words)
	#line = random.choice(group_of_words) + '\n'

	#for i in range(0, len(group_of_words)-1):
		#print(i)
		#print("\n")
	i = random.randrange(1,5)
	results = [x for x in itertools.combinations(group_of_words, i) ]
	random_results = random.choice(results)
	#print(results)
	#print("\n")
	#print("random_results: \n")
	line = (' '.join(random_results) + "\n")


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Shit poster bot for twitter')
	#parser.add_argument('-l', help='number of text lines (default 1)', type=int)
	parser.add_argument('-t, help='time for sleep in seconds (default 300)', type=int)
	args = parser.parse_args()
	t = args.t
	
	while True:

		filename=open('test.txt','w')
		for i in range(3):

			#pick the words
			choosing_words()
			#make the sentences
			phrases()
			#print('adding to file: ' + line)
			filename.write(line)
			
		filename.close()		
		
		filename=open('test.txt','r')
		f=filename.readlines()
		filename.close()
		tweet = f[0] + f[1] + f[2]
		print (tweet)
		#api.update_status(tweet)

		time.sleep(t)

	
	




 





