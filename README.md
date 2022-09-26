# Word Rarity

This script fetches values corresponding to the rarity of English language words. Alternatively, it can be fed input text and return a list of only those words meeting either the default or user-specified conditions for rarity.

## Basic usage

In the simplest use case, this function requires only an input string and it returns a list of tuples, where each tuple contains a single input word and a value corresponding to its rarity. (All input is converted to lower-case and casing is ignored for the purposes of determining rarity.)

> word_rarity("the dog house")

Returns: 

> [('dog', 0.0033393611458529), ('house', 0.009997377423337), ('the', 1.0000000000000002)]

We see "house" is used about three times more frequently than "dog". We also see that "the" has a value of 1, which means "the" is the most common word in our dictionary.

## Other modes

### Aggregate mode

We can also fetch the average rarity of the words in a string by switching the function to aggregate mode.

> word_rarity("the dog house", mode='a')

Returns: 

> 0.33777891285639666

The returned value is the arthimetic mean of the rarity values of the input words. This can be used to compare the language of sentences, paragraphs, articles or longer works.

### Finder mode

The function can also be switched into finder mode, which strips away common words and returns a list containing only the input's rare words.

> word_rarity("Most of these words are common, but three of them, limpid, oeuvre and sesquipedalian, are not.", mode='f')

Returns: 

> ['oeuvre', 'limpid', 'sesquipedalian']

By default, rare words are defined as those falling between the 13th and 95th percentile of the rarity dictionary. This range can be adjusted via the "top" and "bottom" arguments.

> word_rarity("Most of these words are common, but three of them, limpid, oeuvre and sesquipedalian, are not.", mode='f', top=50)

Returns:

> ['sesquipedalian']

Only the rarest of the input's three rare words fell within the adjusted rare range.

Finder mode always uses index data to define rarity, even if the user sets it differently in the function arguments.

## Value types

### Frequency

By default, the function uses "frequency" as its value type to describe word rarity, where smaller numbers indicate greater rarity. Frequency values are pre-generated via a min-max function based on word counts in the original data set used by the word_rarity function. (More on this in the "Data source" section below.)

Alternatively, the value type can be changed to "zscore", "count" or "index".

### Index

The data set used by the function is ordered by word rarity. "The" is at index 0, "pineapple" is at index 15405 and "perspicacious" is at index 268560.

> word_rarity("pineapple", type="index")

Returns: 

> [('pineapple', 15405)]

### Count

The data set's words are ordered according to the number of times they were counted in the original corpus. 

> word_rarity("happy roustabout", type="count")

Returns: 

> [('happy', 63471922), ('roustabout', 47413)]

### Z-score

The data also contains Z-scores as an alternative standardized measure to frequency.

> word_rarity("the sad raconteur", type="zscore")
 
Returns:

> [('raconteur', -0.025691135878988), ('sad', 0.169619810283159), ('the', 348.9316244446038)]

The data types and function modes can also be mixed and matched.

> word_rarity("the sad raconteur", mode="a", type="zscore")

Returns: 

> 116.35851770633599

The exception to this capability is finder mode, which always uses index data.

## Data source

The data used by this function derives from a training corpus of more than one trillion words collected by Google. The data came from public web pages. More on that project can be found [here](https://ai.googleblog.com/2006/08/all-our-n-gram-are-belong-to-you.html). 

The data set used by this function is a reduced version of the Google data shared by the writers of the book Beautiful Data. It contains one-third of a million of the most common English words. More information on that can be found [here](http://norvig.com/ngrams/).

In addition to the one-third of a million words ordered by rarity, the data set used by this function also contains Z-scores, standardized frequency values — ranging between 0 and 1 — based on count values, and the count values themselves, which correspond to the number of times each word was counted in the Google data.



