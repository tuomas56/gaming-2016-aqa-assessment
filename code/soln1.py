from sguigee import *
import random

def load_words():
	with open("Words.txt") as f:
		return list(map(str.strip, f.read().split("\n")))

def chunks(l, n):
#split a list into evenly sized chunks.
    for i in range(0, len(l), n):
        #iterate with a step of n
        yield l[i:i+n]
        #yield a block of length n

def draw_grid(words, c):
	START = (40, 80)
	PADDING = (10, 10)
	for i, x in enumerate(chunks(words, 3)):
		for j, t in enumerate(x):
			c.create_text((START[0] + j*50 + j*PADDING[0], START[1] + i*10 + i*PADDING[1]), text=t)

with window(title="Memory Game!"):
	with row():
		c = canvas(width=200, height=200)
		c.create_text((100, 100), text="Press 'Start' to start.")

	with row():
		@button("Start")
		def start():
			c.clear()
			words = load_words()
			random.shuffle(words)
			words = words[:-1]
			draw_grid(words, c)

