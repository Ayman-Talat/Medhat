# import python libraries
import json
import spacy
from nltk.stem.porter import PorterStemmer
from spellchecker import SpellChecker
import random
from difflib import SequenceMatcher

from SQL.SQLConnection import *


spell = SpellChecker()
stemmer = PorterStemmer()
# Load the English language model
nlp = spacy.load("en_core_web_md")
######################################################################################################################################################
################################# TABLES ##################################
# list of pairs (word, intent)
with open('intents.json', 'r') as f:
    intents = json.load(f)
# list of symbols that to ignore when doing tokenization
ignore_punctuation = ['?', '.', '!', ',', ';', ':', '-', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\'
    , '|', '`', '~', '@', '#', '$', '%', '^', '&', '*', '_', '+', '=', '"', "'"]
# list of pairs (contraction, expanded form)
contractions = [("'m", "am"), ("'s", "is"), ("n't", "not"), ("'ve", "have"), ("can't","cannot")]
affirmations = ["yes", "yeah", "yep", "yup", "sure", "probably", "I think so", 'y']
negations = ["no", "nope", "nah", "not really", "not sure", "negative", "never", "don't", "not", "refuse", "decline",
             "reject", "n"]
pronouns = ['i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them',
            'my', 'a', 'an', 'the', 'your', 'his', 'her', 'its', 'our', 'their', 'mine', 'yours', 'his', 'hers',
            'ours', 'theirs', 'myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves',
            'yourselves', 'themselves']

prepositions = ['at', 'but', 'by', 'for', 'from', 'in', 'of', 'off', 'on', 'out', 'to', 'a', 'an' , 'with']
######################################################################################################################################################
# Data from the Database
DiseasesDB = CallDB("disease", "disease_id")
Disease_Scores = {disease[0]: 100 for disease in DiseasesDB}
del DiseasesDB
user_symptoms = set([])