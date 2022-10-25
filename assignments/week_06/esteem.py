####################
# Date: 2022-10-08
# File: esteem.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: 06 Team Activity: Troubleshooting Functions
# The Rosenberg self-esteem scale
#####################

'''
Assignment
As a team, write a Python program named esteem.py that implements the Rosenberg self-esteem scale. 
Your program must ask the user to respond to each of the ten statements with D, d, a, or A which 
mean strongly disagree, disagree, agree, and strongly agree. Your program must compute the score 
for each answer and sum and display the person's total score. You should think about how you will 
separate this program into functions before you begin writing the program.

Core Requirements
1. Your program prints the introductory text as shown in the Testing Procedure section below.
2. Your program prints each of the ten statements and gets a response from the user.
3. Your program computes the score for each response and sums all the scores and displays the total score.
'''


def main():
    opening_statement = '''
This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.
'''
    print(opening_statement)

    answers = ask_questions()
    # print(answers)

    ###############################
    # TEST DATA
    # answers = ["A", "A", "D", "a", "d", "a", "a", "a", "a", "d"]
    # pos = ["A", "A", "a", "a", "a"] = [3,3,2,2,2] = 12
    # neg = ["D", "d", "a", "a", "d"] = [3,2,1,1,2] = 9
    # total = 12 + 9 = 21
    ################################

    score = calculate_results(answers)

    print(f'''
Your score is {score}.
A score below 15 may indicate problematic low self-esteem.''')


def ask_questions():
    """Loop though list of questions and collect responses.

    Parameters: None
    Return: a list of strings associated with the users inputted answers
    """
    list_array = [
        ("1", "I feel that I am a person of worth, at least on an equal plane with others.", "+")
        ("2", "I feel that I have a number of good qualities.", "+")
        ("3", "All in all, I am inclined to feel that I am a failure.", "-")
        ("4", "I am able to do things as well as most other people.", "+")
        ("5", "I feel I do not have much to be proud of.", "-")
        ("6", "I take a positive attitude toward myself.", "+")
        ("7", "On the whole, I am satisfied with myself.", "+")
        ("8", "I wish I could have more respect for myself.", "-")
        ("9", "I certainly feel useless at times.", "-")
        ("10", "At times I think I am no good at all.", "-")
    ]
    
    list_of_questions = ["I feel that I am a person of worth, at least on an equal plane with others.", "I feel that I have a number of good qualities.", "All in all, I am inclined to feel that I am a failure.", "I am able to do things as well as most other people.",
                         "I feel I do not have much to be proud of.", "I take a positive attitude toward myself.", "On the whole, I am satisfied with myself.", "I wish I could have more respect for myself.", "I certainly feel useless at times.", "At times I think I am no good at all."]

    list_of_options = '''
    Do you:
    D - strongly disagree with the statement.
    d - disagree with the statement.
    a - agree with the statement.
    A - strongly agree with the statement.
    '''

    answers = []
    for q in list_of_questions:
        questions = input(f"\n {q}\n {list_of_options}")
        answers += [questions]

    return answers


def calculate_results(answers):
    """Calculate the users response into a numerical score.

    Parameters:
        answers:  a list of string responses from the user.
    Return: the score from the users response
    """
    a = answers
    positive = [a[0], a[1], a[3], a[5], a[6]]
    negative = [a[2], a[4], a[7], a[8], a[9]]

    pos_score = []
    for i in positive:
        if i == "D":
            pos_score += [0]
        elif i == "d":
            pos_score += [1]
        elif i == "a":
            pos_score += [2]
        elif i == "A":
            pos_score += [3]
        else:
            None

    neg_score = []
    for i in negative:
        if i == "D":
            neg_score += [3]
        elif i == "d":
            neg_score += [2]
        elif i == "a":
            neg_score += [1]
        elif i == "A":
            neg_score += [0]
        else:
            None

    pos_sum = sum(pos_score)
    neg_sum = sum(neg_score)

    # print(pos_score, pos_sum)
    # print(neg_score, neg_sum)

    score = pos_sum + neg_sum

    return score


def get_valid_response():
    response = input('Your response (D, d, a, A): ')
    while response not in ['D', 'd', 'a', 'A']:
        print('Do you "Strongly Disagree" ("D"), "Disagree" ("d"), "Agree" ("a"), or "Strongly Agree" ("A")?')
        response = input('Your response (D, d, a, A): ')
    return response


# Call the main function so that
# this program will start executing.
if __name__ == "__main__":
    main()
