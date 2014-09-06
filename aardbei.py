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
# make a multiple choice question
# deliver to user
## accept user choice
## judge and return 
