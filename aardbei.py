#! /usr/bin/env python3
import random

# some constants that maybe we'll change
NUM_OPTIONS = 4

# I/O from user
# read in and parse sentences

filename = 'sentences'
with open(filename) as f:
    sentences = f.readlines()

filename = 'definitions'
with open(filename) as f:
    definitions = f.readlines()



# read in and parse definitions

# assemble woord objects
class woord:
    def __init__(self,nederlands, engels, zin, tags = None):
        self.nederlands = nederlands
        self.engels = engels
        self.zin = zin
        self.tags = tags
    
    def __repr__(self):
        return 'woord({0},{1},{2},{3},{4})'.format(self.nederlands,
                                                   self.engels,
                                                   self.zin,
                                                   self.tags,
                                                   self.gender)

    def __str__(self):
        return self.nederlands


# make a multiple choice question
def get_woorden(woorden, tags, blacklist = set()):
    return [w for w in woorden if tags.issubset(w.tags) and w not in blacklist]

def ask_question(woorden, tags, known = "nederlands"):
    '''Present the user with a question based on the tags they specified.
    Distractors should have the same tags.'''
    # select a potential words
    goed_woorden = get_woorden(woorden, tags)
    options = random.sample(goed_woorden, NUM_OPTIONS)
    ans = options[0]
    if known == 'nederlands':
        qWoord = ans.nederlands
        CorrectWoord = ans.engels
        distractors = [o.engels for o in options[1:]]
    else:
        qWoord = ans.engels
        CorrectWoord = ans.nederlands
        distractors = [o.nederlands for o in options[1:]]
    qline = 'Choose the definition: {0}'.format(qWoord)
    olines = random.shuffle([CorrectWoord] + distractors)
    print(qline)
    for i,o in enumerate(olines):
        print('{0}. {1}'.format(i,o))
    guess = input('Your Answer? ')    
    if olines[int(guess)-1] == CorrectWoord:
        print('Jij hebt geluk!')
    else:
        print('Het spijt mij.  The answer was {0}.'.format(CorrectWoord)
    




# deliver to user
## accept user choice
## judge and return 
