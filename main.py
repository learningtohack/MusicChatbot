from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from textblob import TextBlob
 
import sys
import spotipy
import spotipy.util as util

import random

from moodtape_functions import authenticate_spotify, aggregate_top_artists, aggregate_top_tracks, select_tracks, create_playlist
import h5py
from tensorflow import keras
from keras.models import load_model
best_model = load_model("best_model1.hdf5")

bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# bot.set_trainer(ListTrainer)
# bot.set_trainer(ChatterBotCorpusTrainer)
trainer = ListTrainer(bot)
# bot.train(['What is your name?', 'My name is Candice'])
# bot.train(['Who are you?', 'I am a bot' ])
# bot.train(['Who created you?', 'Tony Stark', 'Sahil Rajput', 'You?'])
trainer.train([
	"Hi",
    "How are you?",
    "I am good",
    "That is good to hear",
    "I know"
    "Would you like to hear happy songs now?",
    "Yes I would love to",
    "How is the weather?",
    "It is very pleasant",
    "Do you like pop music?",
    "Not much",
    "What all genres do you like?",
    "Classical, blues, jazz",
    "That's awesome.",
    "Bye",
    "Bye"
])
# trainer.train("chatterbot.corpus.english")

# def pred(txt):
# 	blob=TextBlob(txt);
# 	return blob.polarity


client_id = "bc6ce56c9c874a419223b362e04db182"
client_secret = "e81091e7e0d644d397086ddd11633aff"
redirect_uri = "http://localhost:5000/"

scope = 'user-library-read user-top-read playlist-modify-public user-follow-read'

username = "31nkfasf3a62dvm54smtubxgdvpu"
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)


STATIC_FOLDER = 'templates/assets'

app = Flask(__name__,static_folder=STATIC_FOLDER)

@app.route('/')
def my_form():
    return render_template('input.html')

@app.route('/home')
def home():
    return render_template('index2.html')

mood=0.5



sentiment = [0,-1,1]
def predict(line):
  sequence = tokenizer.texts_to_sequences(line)
  test = pad_sequences(sequence, maxlen=max_len)
  return sentiment[np.around(best_model.predict(test), decimals=0).argmax(axis=1)[0]]

@app.route("/get")
def get_bot_response():
	global mood
	userText = request.args.get('msg')
	val=predict(userText)
	if(val > 0):
		mood = mood + 0.5;
	else:
		mood = mood - 0.1;
	if(mood>1):
		mood=random.uniform(0.5,1)
	if(mood<0):
		mood=random.uniform(0,0.5)
	return str(bot.get_response(userText)) 

@app.route("/", methods=['POST'])
def moodtape():
	global mood
	# mood = request.form['text']
	# username = request.form['username']
	print(mood)
	# token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
	spotify_auth = authenticate_spotify(token)
	top_artists = aggregate_top_artists(spotify_auth)
	top_tracks = aggregate_top_tracks(spotify_auth, top_artists)
	selected_tracks = select_tracks(spotify_auth, top_tracks, mood)
	playlist = create_playlist(spotify_auth, selected_tracks, mood)
	return render_template('playlist.html', playlist=playlist )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
