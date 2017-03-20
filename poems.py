import tweepy, time, sys
import random, itertools
import words


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


random_number = random.randrange(1,3)

#def printing(verb, adverb, adverb_word, thing, things_word)

verb_word = 0
adverb_word = 0
things_word = 0
wheather_word = 0
ly_word = 0
prepositions_word = 0
fuckyoupython = 0
line = 0


def choosing_words():

	global verb_word
	global adverb_word
	global things_word
	global wheather_word
	global ly_word
	global prepositions_word
	global fuckyoupython

	verbs = (words.base, words.past_Participle, words.past_Simple)
	adverbs = (words.adverbs_of_Quantity, words.adverbs_of_Cause, words.adverbs_of_Place, words.adverbs_of_Time)
	things = (words.body, words.animals, words.buildings, words.clothes, words.downtown)
	fuckyoupython = 'youfuckingfuck'
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
	prepositions_word = random.choice(words.prepositions)



def phrases():

	global line

	group_of_words = [verb_word, adverb_word, things_word, wheather_word, ly_word, prepositions_word]
	random.shuffle(group_of_words)

	"""	a = verb_word
	b = adverb_word
	c = things_word
	d = wheather_word
	e = ly_word"""


	type_a = verb_word
	type_b = adverb_word
	type_c = things_word
	type_d = wheather_word
	type_e = ly_word

	type_f = (verb_word + ' ' + adverb_word + ' ' + things_word)
	type_g = (verb_word + ' ' + adverb_word + ' ' + wheather_word)
	type_h = (things_word + ' ' + wheather_word + ' ' + ly_word)
	type_i = (things_word + ' ' + ly_word + ' ' + prepositions_word)
	type_j = (wheather_word + ' ' + adverb_word + ' ' + verb_word)
	type_k = (ly_word + ' ' + things_word + ' ' + prepositions_word)


	types = [type_a, type_b, type_c, type_d, type_e, type_f, type_g, type_h, type_i, type_j, type_k]
	line = random.choice(types) + '\n'


def main():
	global line
	
	while True:
		filename=open('test.txt','w')
		for i in range(3):
			choosing_words()
			phrases()
			print('adding to file: ' + line)
			filename.write(line)
			
		filename.close()		
		

		filename=open('test.txt','r')
		f=filename.readlines()
		filename.close()
		tweet = f[0] + f[1] + f[2]
		print (tweet)
		api.update_status(tweet)

		time.sleep(900)

	
	




main()



 





