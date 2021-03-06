"""Generate Markov text from text files."""
import sys

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as opened_file:
        read_file = opened_file.read()

    return read_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    text_string = open_and_read_file(input_path)
    text_words = text_string.split()

    """for index in range(len(text_words) - 2):

        bigram = tuple([text_words[index], text_words[index + 1]])
        following_word = text_words[index + 2]

        if bigram in chains:  # if key in dict, append to existing value
            chains[bigram].append(following_word)

        else:
            chains[bigram] = [following_word]  # init value of key as a list
"""
    # ngram_type = what sort of ngram user decides
    # ngrams = a list of the words to be tupled into a dict key
    # ngram_key = the actual ngram in the dictionary

    ngram_type = int(raw_input("What kind of ngram do you want to use? > "))

    for index in range(len(text_words) - ngram_type):
        ngrams = []

        for num in range(ngram_type):
            ngrams.append(text_words[index + num])

        ngram_key = tuple(ngrams)
        following_word = text_words[index + ngram_type]

        if ngram_key in chains:
            chains[ngram_key].append(following_word)

        else:
            chains[ngram_key] = [following_word]

    # print "THIS IS OUR LIST OF NGRAMS:", ngrams
    # print "THIS IS OUR NGRAM:", ngram_key

    return chains


def make_text(chains):
    """Return text from chains."""

    #chains = make_chains(input_text)

    words = []

    """
    random_bigram = choice(chains.keys())

    for word in random_bigram:
        words.append(word)

    while random_bigram in chains:
        following_word = choice(chains[random_bigram])
        words.append(following_word)

        random_bigram = (random_bigram[1], following_word)

    """

    random_ngram = choice(chains.keys())

    for word in random_ngram:
        words.append(word)

    while random_ngram in chains:
        following_word = choice(chains[random_ngram])
        words.append(following_word)

        random_ngram = random_ngram[1:].append(following_word)

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print chains
