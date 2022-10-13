####################
# Date: 2022-10-08
# File: sentences.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: 05 Prove Milestone: Testing and Fixing Functions
#####################

import random

"""
Write and test functions that generate sentences with three parts:
    1. a determiner (sometimes known as an article)
    2. a noun
    3. a verb

For example:
    A cat laughed.
    One man eats.
    The woman will think.
    Some girls thought.
    Many dogs run.
    Many men will write.

Write the main function and any other functions 
that you think are necessary for your program to 
generate and print six sentences with these characteristics:

Quantity	Verb Tense
a.	single	past
b.	single	present
c.	single	future
d.	plural	past
e.	plural	present
f.	plural	future
"""

def main():

    """Call the get_random_sentence_generator function
    generate a random number of sentences with specified parameter"""
    #random_sentence_generator(20)

    """Call the get_sentence_by_list function
    generate sentences with the parameters specified in the list"""
    get_sentence_by_list()

    """Call the get_sentence function
    generate one sentence with parameters specified"""
    # get_sentence(0, "past")

def get_sentence(quantity, tense):
    '''Returns a randomly generated word by calling
    get_determiner, get_noun, get_verb.
    Parameter
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: prints a randomly generated sentence.
    '''
    d = get_determiner(quantity).capitalize()
    n = get_noun(quantity)
    v = get_verb(quantity, tense)

    sentence =(f"{d.capitalize()} {n} {v}.")
    print(sentence)


def get_sentence_by_list():
    '''Returns a randomly generated word by calling
    get_determiner, get_noun, get_verb.
    Parameter
        None - update list to determine sentence structure and length.
    Return: prints a number of randomly generated sentences.
    '''
    list = [(1, "past"), (1, "present"), (1, "future"), (0, "past"), (0, "present"), (0, "future")]
    
    for quantity, tense in list:
        d = get_determiner(quantity).capitalize()
        n = get_noun(quantity)
        v = get_verb(quantity, tense)

        sentence =(f"{d.capitalize()} {n} {v}.")
        print(sentence)

def random_sentence_generator(number=7):
    '''Returns a randomly generated word by calling
    get_determiner, get_noun, get_verb.
    Parameter
        number: an integer.
            The default is 7
    Return: prints a number of randomly generated sentences.
    '''
    quantity = random.choice([0,1])
    tense = random.choice(["past", "present", "future"])

    for _ in range(number):
        d = get_determiner(quantity).capitalize()
        n = get_noun(quantity)
        v = get_verb(quantity, tense)

        sentence =(f"{d.capitalize()} {n} {v}.")
        print(sentence)


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    noun = random.choice(nouns)
    return noun



def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if (quantity != 1 or quantity == 1) and tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif quantity == 1 and tense == "present":
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif quantity != 1 and tense == "present":
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif (quantity != 1 or quantity == 1) and tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # Randomly choose and return a verb.
    verb = random.choice(verbs)
    return verb



# Call the main function so that
# this program will start executing.
if __name__ == "__main__":
    main()
