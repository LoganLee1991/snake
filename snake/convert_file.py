#!/usr/bin/env python

import tokenize
import argparse
from sys import argv

from snake.replace_emoji import replace_emoji
import snake.python_to_emoji as python_to_emoji

try:
    f = open(argv[1], 'rb')
except IndexError:
    print("Please enter a file to convert")
    exit()

tokens = tokenize.tokenize(f.readline)
emojified = python_to_emoji.replace_text(tokens)

out = open("tokens.out", 'w')
out.write(str(emojified))

out.close()

emojipython = open("tokens.out", 'rb')
python = tokenize.untokenize(emojified)
print(python.decode())

out = open("emoji-python.py", 'w')
out.write(str(python.decode()))


out.close()
emojipython.close()
