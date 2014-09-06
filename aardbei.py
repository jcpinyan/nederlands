#! /usr/bin/env python3

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
# deliver to user
## accept user choice
## judge and return 
