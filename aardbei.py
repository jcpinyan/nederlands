#! /usr/bin/env python3

# I/O from user
# read in and parse sentences

filename = 'sentences'
with open(filename) as f:
    sentences = f.readlines()

def sentenceStripper(line):
    '''gets the words from a sentence'''
    zin = line.strip()
    for punc in [',', '.', '!', '?']:
        zin = zin.replace(punc,'')
    zin = zin.lower()
    woorden = set(zin.split())
    return(woorden)
    

filename = 'definitions'
with open(filename) as f:
    definitions = f.readlines()



# read in and parse definitions

# assemble woord objects
class woord:
    def __init__(self,nederlands, engels, zin, tags = None, gender = None):
        self.nederlands = nederlands
        self.engels = engels
        self.zin = zin
        self.tags = tags
        self.gender = gender
    
    def __repr__(self):
        return 'woord({0},{1},{2},{3},{4})'.format(self.nederlands,
                                                   self.engels,
                                                   self.zin,
                                                   self.tags,
                                                   self.gender)

    def __str__(self):
        return self.nederlands


# make a multiple choice question
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
