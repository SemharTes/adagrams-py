##-----------------------------------------##
##-----------------WAVE 1------------------##
##-----------------------------------------##
"""
1. Your first task is to build a hand of 10 letters for the user. 
-No parameters
-Returns an array of ten strings
    -Each string should contain exactly one letter
    -These represent the hand of letters that the player has drawn
-The letters should be randomly drawn from a pool of letters
    -This letter pool should reflect the distribution of letters as described in the table below
    -There are only 2 available C letters, so draw_letters cannot ever return more than 2 Cs
    -Since there are 12 Es but only 1 Z, it should be 12 times as likely for the user to draw an E as a Z
-Invoking this function should not change the pool of letters
    -Imagine that the user returns their hand to the pool before drawing new letters
    reference: https://theprogrammingexpert.com/get-random-value-from-dictionary-python/
"""
import random

def draw_letters():
    # string == 1letter only
    # hand_letter == [ten strings]
    # draw_letters.random(LETTER_POOL)
    # return an array of hand_letter

    LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 
    'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 
    'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 
    'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
    'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 
    'Z': 1
}
    letters = []
    letter_frequency = {}
    for i in range(11):
        letter = random.choice(list(LETTER_POOL)) 
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
        if letter_frequency[letter] <= LETTER_POOL[letter]:
            letters.append(letter)
        if len(letters) == 10:
            break
    print(len(letters))
    return letters
    
    
##-----------------------------------------##
##-----------------WAVE 2------------------##
##-----------------------------------------##
"""
2. You need a way to check if an input word (a word a player submits) only uses characters that 
    are contained within a collection (or hand) of drawn letters
-Has two parameters:
    -word, the first parameter, describes some input word, and is a string
    -letter_bank, the second parameter, describes an array of drawn letters in a hand. You can expect this to be an array of ten strings,
    with each string representing a letter
-Returns either True or False
-Returns True if every letter in the input word is available (in the right quantities) in the letter_bank
-Returns False if not; if there is a letter in input that is not present in the letter_bank or has too much of compared to the letter_bank
reference: https://www.programiz.com/python-programming/methods/list/count
"""

def uses_available_letters(word, letter_bank):
    # ensure consistent case
    word = word.upper()
    # check input word is anagram within drawn letters
    #iterating over each letter in the word
    for letter in word:
        # check if that letter is in the letter bank
        if letter in letter_bank:
            word_count = word.count(letter)
            # if word_count is in the right quantities in the letter bank, continue checking next letter
            if word_count == letter_bank.count(letter):
                continue
            else:
                return False
        else:
            return False
    return True


##-----------------------------------------##
##-----------------WAVE 3------------------##
##-----------------------------------------##
"""
3. Now you need a function returns the score of a given word as defined by the Adagrams game.
-Has one parameter: word, which is a string of characters
-Returns an integer representing the number of points
-Each letter within word has a point value. The number of points of each letter is summed up to represent the total score of word
-Each letter's point value is described in the table below
-If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points
"""
def score_word(word):
    score_chart = {"A":1, "E":1, "I":1, "O":1, "U":1, "L":1, "N":1, "R":1, "S":1, "T":1, "D":2,
    "G":2, "B":3, "C":3, "M":3, "P":3, "F":4, "H":4, "V":4, "W":4, "Y":4, "K":5, "J":8, "X":8,
    "Q":10, "Z":10
    }
    score = 0
    if len(word) >=7:
            score += 8
    for letter in word:
        score += score_chart[letter.upper()]
            
    return score



##-----------------------------------------##
##-----------------WAVE 4------------------##
##-----------------------------------------##
"""
4. You need a way to find the highest scoring word. This function looks at the list of word_list and calculates which 
    of these words has the highest score, applies any tie-breaking logic, and returns the winning word in a special 
    data structure.
-Has one parameter: word_list, which is a list of strings
-Returns a tuple that represents the data of a winning word and it's score. The tuple must contain the following elements:
    -index 0 ([0]): a string of a word
    -index 1 ([1]): the score of that word
-In the case of tie in scores, use these tie-breaking rules:
    -prefer the word with the fewest letters...
    -...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, 
        choose the one with 10 letters over the one with fewer tiles
    -If the there are multiple words that are the same score and the same length, pick the first one in the supplied list
    reference: https://www.geeksforgeeks.org/python-difference-between-sorted-and-sort/
    https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
"""
def get_highest_word_score(word_list):    


    # word, pos = max(word_list, key=highest_score)
    # tuple_highest_word.append(word, pos)
    # return tuple_highest_word
# return max(word_list, key=get_value)
# def get_value(word):
#     """Return word letter score."""
#     return sum(score_chart[letter] for letter in word)

    score = []
    highest_scores = []

    for i in range(len(word_list)):
        if i > 0:
            if score_word(word_list[i]) > score[1]:
                highest_scores.clear()
                score = [word_list[i], score_word(word_list[i])]
                highest_scores.append(score)
            elif score_word(word_list[i]) == score[1]:
                score = [word_list[i], score_word(word_list[i])]
                highest_scores.append(score)
            else:
                continue
        else:
            score = [word_list[i], score_word(word_list[i])]
            highest_scores.append(score)

    if len(highest_scores) == 1: # highest_score = [[word_list[i], score_word(word_list[i])]]
        return highest_scores[0]
    elif len(highest_scores) > 1:
        print(f"highest scores before sort {highest_scores}")
        highest_scores = sorted(highest_scores, key = lambda x: len(x[0]))
        print(f"highest scores after sort {highest_scores}")
        for i in range(len(highest_scores)):
            if len(highest_scores[i][0]) >= 10:
                return highest_scores[i]
        return highest_scores[0]
