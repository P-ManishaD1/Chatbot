import pandas as pd
import nltk
import string
import difflib
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(tag):
    if tag.startswith('J'): return wordnet.ADJ
    elif tag.startswith('V'): return wordnet.VERB
    elif tag.startswith('N'): return wordnet.NOUN
    elif tag.startswith('R'): return wordnet.ADV
    else: return wordnet.NOUN

# Preprocess a single question
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in string.punctuation and t not in stop_words]
    pos_tags = pos_tag(tokens)
    lemmatized = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]
    return '-'.join(lemmatized)

# Step 1 to 7: Read CSV, process questions, map to answers, write to new file
def prepare_data(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df['Processed_Question'] = df['question'].apply(preprocess)
    df[['Processed_Question', 'answer']].to_csv(output_csv, index=False)

# Step 3 in Module-2: Match question using fuzzy
def get_response(user_question, df):
    user_processed = preprocess(user_question)
    all_questions = df['Processed_Question'].tolist()
    best_match = difflib.get_close_matches(user_processed, all_questions, n=1, cutoff=0.6)
    if best_match:
        matched_row = df[df['Processed_Question'] == best_match[0]]
        return matched_row['answer'].values[0]
    else:
        return "Sorry, I couldn't find an answer to your question."
