import numpy as np
import pandas as pd
from rake_nltk import Rake
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer

df = pd.read_csv("/Users/benjamingoldblatt/webscraper/bbookscleaned.csv")

df['Bag_of_words'] = ''
columns = ['genres', 'authors', 'Key_words'] 
for index, row in df.iterrows():
    words = ""
    for col in columns:
        entries = row[col]
        entries = eval(entries)
        for word in entries:
            words = words + " " + word
    df.loc[index, 'Bag_of_words'] = words
df = df[['title', 'Bag_of_words']]

df.to_csv('bbooksdescr.csv', index = False)
'''
for index, row in df.iterrows():
    lemmatizer = WordNetLemmatizer()
    plot = row['Key_words']
    plot = eval(plot)
    lem = []
    for w in plot:
        lem.append(lemmatizer.lemmatize(w))
    df.at[index, 'Key_words'] = lem

for index, row in df.iterrows():
    lemmatizer = WordNetLemmatizer()
    plot = row['authors']
    plot = eval(plot)
    lem = []
    for w in plot:
        lem.append(''.join(w.split()).lower()
)
    df.at[index, 'authors'] = lem

df['Key_words'] = ""
for index, row in df.iterrows():
    plot = row['description']
    
    # instantiating Rake, by default it uses english stopwords from NLTK
    # and discards all puntuation characters as well
    r = Rake()

    # extracting the words by passing the text
    r.extract_keywords_from_text(plot)

    # getting the dictionary whith key words as keys and their scores as values
    key_words_dict_scores = r.get_word_degrees()
    

    # assigning the key words to the new column for the corresponding movie
    row['Key_words'] = list(key_words_dict_scores.keys())
    df.at[index, 'Key_words'] = row['Key_words']


# dropping the Plot column
df.drop(columns = ['description'], inplace = True)


df.to_csv('bbcleaned.csv', index = False)
'''