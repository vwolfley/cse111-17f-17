####################
# Date: 2022-10-08
# File: test_sentences.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: 05 Prove Milestone: Testing and Fixing Functions
#####################


from sentences import get_determiner, get_noun, get_verb
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
    
def test_get_noun():
    # test single nouns.
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # Call the get_noun function which should return a single noun.
    for _ in range(11):
        noun = get_noun(1)
        # Verify that the noun returned from get_noun is one of the words in the single_nouns list.
        assert noun in single_nouns

    # test plural nouns.
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Call the get_noun function which should return a plural noun.
    for _ in range(11):
        noun = get_noun(2)
        # Verify that the noun returned from get_noun is one of the words in the plural_nouns list.
        assert noun in plural_nouns
    
    
def test_get_verb():
    # test past tense verbs.
    past_tense_verb = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    # Call the get_verb function which should return a single past tense verb.
    for _ in range(11):
        verb = get_verb(0, "past")
        # Verify that the verb returned from get_verb is one of the words in the past_tense_verb list.
        assert verb in past_tense_verb

    # test present tense singular verb.  
    # A singular verb is one that has an s added to it in the present tense.
    present_tense_singular_verb = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    # Call the get_verb function which should return a single present tense singular verb.
    for _ in range(11):
        verb = get_verb(1, "present")
        # Verify that the verb returned from get_verb is one of the words in the past_tense_verb list.
        assert verb in present_tense_singular_verb
    
    # test present tense plural verb.
    # A plural verb does not have an s added to it in the present tense.
    present_tense_plural_verb = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    # Call the get_verb function which should return a single present tense plural verb.
    for _ in range(11):
        verb = get_verb(2, "present")
        # Verify that the verb returned from get_verb is one of the words in the present_tense_plural_verb list.
        assert verb in present_tense_plural_verb

    # test future tense verb.
    future_tense_verb = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # Call the get_verb function which should return a single future tense verb.
    for _ in range(11):
        verb = get_verb(0, "future")
        # Verify that the verb returned from get_verb is one of the words in the future_tense_verb list.
        assert verb in future_tense_verb




# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])