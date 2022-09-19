import pandas as pd
import re

df = pd.read_csv('word_rarity_list.csv')
dict_size = df['word'].size

def strip_character(a_string):
    r = re.compile(r"[^a-zA-Z- ]")
    return r.sub(' ', a_string)

def remove_spaces(a_string):
    return re.sub(' +', ' ', a_string)

def remove_apos_s(a_string):
    return re.sub("'s", '', a_string)

def clean_input_text(input_text):
    # convert input to lowercase
    input_text = input_text.lower()
    # remove apostrophe-s from words
    input_text = remove_apos_s(input_text)
    # strip non-essential characters
    input_text = strip_character(input_text)
    # remove internal spaces
    input_text = remove_spaces(input_text)
    # remove end spaces
    input_text = input_text.strip()
    return input_text

def tokenize(cleaned_text):
    # split string on spaces
    tokens = cleaned_text.split(" ")
    # create empty set
    token_set = set()
    # add one of each unqiue word from 'tokens' to set
    for word in tokens:
        if word in token_set:
            pass
        else:
            token_set.add(word)
    return token_set

# returns rarity values of each word
# frequency, zscore, count, index
def fetch_rarity(input_text, type):
    results = []
    for word in input_text:
        fetched_values = df[df['word'] == word]
        if fetched_values.size == 0:
            results.append((word, 0))
        else:
            if type == 'zscore':
                results.append((word, fetched_values['zscore'].values[0]))
            elif type == 'count':
                results.append((word, fetched_values['count'].values[0]))
            elif type == 'index':
                results.append((word, fetched_values.index.values[0]))
            else:
                results.append((word, fetched_values['frequency'].values[0]))
    return results

def fetch_mean(tuple_list):
    running_total = 0.0
    size = len(tuple_list)
    for tuple in tuple_list:
        running_total += tuple[1]
    list_mean = running_total/size
    return list_mean

def rare_finder(tuple_list, top, bottom):
    rare_words = []
    bottom_index = round(dict_size * (bottom/100))
    top_index = round(dict_size * (top/100))
    for tuple in tuple_list:
        if tuple[1] >= top_index and tuple[1] <= bottom_index:
            rare_words.append(tuple[0])
        elif tuple[1] == 0:
            rare_words.append(tuple[0])
    return rare_words

#   'w' word mode returns rarity values for each word
#   'a' aggregate mode returns average rarity values
#   'f' finder mode returns words within rare range
def word_rarity(input_text, mode='w', type='frequency', top=13, bottom=95):
    if mode == 'f':
        type = 'index'
    cleaned_input_text = clean_input_text(input_text)
    tokens = tokenize(cleaned_input_text)
    token_values = fetch_rarity(tokens, type)
    if mode == 'a':
        mean_of_tokens = fetch_mean(token_values)
        return mean_of_tokens
    elif mode == 'f':
        rare_words = rare_finder(token_values, top, bottom)
        return rare_words
    else: #'w'
        return token_values

