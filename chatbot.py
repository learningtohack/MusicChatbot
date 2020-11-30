#toolbox
import os

import tensorflow as tf
from tensorflow import keras
import random
from textblob import TextBlob


#1. Name and nickname conversation
print('Hello human what is your name?')
name = input()
print('')
print('Do you have a nickname Y/N?')
ans = input()
print('')

if ans.lower() == 'yes' or ans.lower() == 'y':
	print('what is your nickname?')
	nickname = input()
	print('Nice to meet you',nickname)
else:
	nickname =  name + ' ' + name +'y'
	print('I will call you ' + nickname)

print('')

#2. Greeting random selection and polarity based response
questions = [
	'So '+ nickname + ' how are you today?',
	'Howdy '+ nickname +' how are you feeling?',
	"So " + nickname + " what's up with you?",
	'Greetings human, are you well?',
	'So '+ nickname + ' how are things going?'
]

print(random.choice(questions))
ans = input()
print('')
blob = TextBlob(ans)
# blob = preprocess(blob)
if blob.polarity > 0:
	print('I am glad that you are well')
else:
	print(nickname, "that doesn't sound so good")
#-1 0 1

#3. Random qestion on a random topic
topics = [
	'football',
	'this weather',
	'Melbourne',
	'The Joker',
	'Endgame',
	'Python',
	'computer games',
	'chatbots'
]

questions = [
	'What is your take on ',
	'What do you think about ',
	'How do you feel about ',
	nickname + ' do you like ',
	'I would like your opinion on ',
	'I would love to know what you think about '
]

new_model = tf.keras.models.load_model('best_model1.hdf5')
def predict(line):
  sequence = tokenizer.texts_to_sequences(line)
  test = pad_sequences(sequence, maxlen=max_len)
  sentiment[np.around(new_model.predict(test), decimals=0).argmax(axis=1)[0]]

for i in range(0,random.randint(2,4)):
	topic = random.choice(topics)
	topics.remove(topic)
	question = random.choice(questions)
	questions.remove(question)
	print(question + topic + '?')
#4. Response to random question using sentiment analysis
	ans = input()
	listans=[ans]
	print(predict(list1))
	# blob = TextBlob(ans)
	

# 3. Respond appropriately to positive and negative sentiment
	# if blob.polarity > 0.5:
	# 	a = 'Wow you really love '+ topic
	# elif blob.polarity > 0.1:
	# 	a = 'Cool you like '+ topic
	# elif blob.polarity < -0.1:
	# 	a = 'Hmm, not a fan of '+ topic
	# elif blob.polarity < -0.5:
	# 	a = 'So you hate '+ topic
	# else:
	# 	a = 'That is a very neutral view on '+ topic

	# if blob.subjectivity > 0.6:
	# 	print(a + ' and you are totally biased')
	# elif blob.subjectivity > 0.3:
	# 	print(a + ' and you are a bit biased')
	# else:
	# 	print(a + ' and quite objective')

print('')

#5. Random goodbye 
goodbyes = [
	'Catch ya later ' + nickname,
	'Nice chatting yo you ' + name + ' I am off now',
	'Yaawn, I am tired of chatting with you, bye bye',
	'Good talk my friend, see you next time'
	'That was a pleasant chat ' + name + ' goodbye for now'
]

print(random.choice(goodbyes))
