import random

LIST = "words.txt"
word_list = []


def retrieve_word():
    with open(LIST, 'r') as f:
        for line in f:
            word_list.extend(line.split())
    return random.choice(word_list)


