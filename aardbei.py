#! /usr/bin/env python3
from collections import defaultdict
import random

# some constants that maybe we'll change
NUM_OPTIONS = 4

# I/O from user
# read in and parse sentences


def sentenceStripper(line):
    '''gets the words from a sentence'''
    zin = line.strip()
    for punc in [',', '.', '!', '?']:
        zin = zin.replace(punc,'')
    zin = zin.lower()
    woorden = set(zin.split())
    return(woorden)


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




def get_woorden(woorden, tags, blacklist = set()):
    '''Return a list of woorden that have all the desired tags.'''
    return [w for w in woorden if tags.issubset(w.tags) and w not in blacklist]

# make a multiple choice question
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
    
## user indicates desired tag (or all)
## script chooses a woord with that tag
### script chooses 3 distractors with that tag
### script grabs English definition
## script makes pretty question
## user enters an answer
### if answer is correct, deliver prize
### if answer is wrong, deliver sentence and retest
### if answer is wrong a second time, 
#### deliver sentence 
#### deliver answer with Dutch word
#### deliver distractors with Dutch words



filename = 'sentences'
with open(filename) as f:
    sentences = f.readlines()

zinDict = defaultdict(list)
for line in sentences:
    if not line.startswith('#'):
        for i in sentenceStripper(line): zinDict[i].append(line.strip())

filename = 'definitions'
with open(filename) as f:
    definitions = f.readlines()


