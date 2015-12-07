from sguigee import *
import random
import time

def load_words(extended:bool=False) -> list:
	with open("WordsExt.txt" if extended else "Words.txt") as f:
		return list(map(str.strip, f.read().split("\n")))[:-1]
		#read the contents of the file 'f.read()'
		#split it at the newlines '.split("\n")'
		#remove excess spaces on either side 'map(str.strip'

def chunks(l, n):
#chunks(l:list[T], n:int) -> iterator[slice[T]]
    for i in range(0, len(l), n):
        yield l[i:i+n]

def draw_grid(words:list, c:canvas, n:int) -> None:
	PADDING = (10, 10)
	#padding between words
	offset_x = (50*len(words)/n - PADDING[0] * (n - 1)) / 2
	#Assuming a word is 50 pixels, space out n words and n - 1 paddings between them, then halve.
	offset_y = (20*len(words)/n - PADDING[1] * (n - 1)) / 2
	#Same here, assuming a word is 20 pixels high
	START = (200 - offset_x, 200 - offset_y)
	#start at the middle minus the offsets
	for i, x in enumerate(chunks(words, n)):
		for j, t in enumerate(x):
			c.create_text((START[0] + j*50 + (j-1)*PADDING[0], START[1] + i*20 + (i-1)*PADDING[1]), text=t)
			#start + word in row * 50 + word in row - 1 * padding

def play_game(words, size):
	with window(title="Memory Game", can_resize=False) as w:
		with row():
			c = canvas(width=400, height=400)
			c.create_text((200, 200), text="Press 'Start' to start.")

		with row() as r:
			@button("Start")
			def start():
				c.clear()
				r.destroy()
				#destroying the button only leaves a gap so destroy the actual frame.
				nonlocal words
				random.shuffle(words)
				words, to_replace = words[:-1], words[-1]
				#shave of the last word and use that one to replace another later,
				#since the number of words in the list is one more than we need.
				draw_grid(words, c, size)

				@after(30)
				def then():
					words[-1], replaced = to_replace, words[-1]
					#now replace the last word (in the nine-element list, not ten) with the word we got earlier
					random.shuffle(words)
					#and shuffle it so its not always the last one
					c.clear()
					draw_grid(words, c, size)
					@after(5)
					def then():
						guessed_removed = ask_word('What word was removed?', replaced)
						guessed_replaced = ask_word('What was it replaced with?', to_replace)
						if guessed_removed and guessed_replaced:
							end_game(c, True, True)
						elif guessed_removed:
							end_game(c, True, to_replace)
						elif guessed_replaced:
							end_game(c, replaced, True)
						else:
							end_game(c, replaced, to_replace)

						with row():
							@button('Return to Menu')
							def done():
								w.get().destroy()

def ask_word(prompt, word, guesses=3):
	prompt = '%s You have %%s guesses remaining.' % prompt
	#string interpolation is faster than using +=
	#we use %%s here because we are going to interpolate twice, and this will yield a literal
	#%s character.
	for i in range(guesses, 0, -1):
	#we use range with a negative step to read backwards over the range from guesses to zero
	#i.e) i = 3, 2, 1
		guess = ask_message(prompt % i)
		if guess == word:
			return True
	return False

def end_game(c, removed, replaced):
	#if a word is guessed, it is True else it is the word it should have been.
	c.clear()
	if removed is True:
		#we use 'is True' here since a non empty string would also compare true if we used ==
		#i.e) bool('some string') is True
		c.create_text((200, 100), text='You remembered which\nword was removed!')
	else:
		c.create_text((200, 100), text='The word which\nwas removed was %s' % removed)

	if removed is True:
		c.create_text((200, 150), text='You remembered which\nword replaced it!')
	else:
		c.create_text((200, 150), text='The word which\nreplaced it was %s' % replaced)

def menu():
	with window('Menu') as w:
		with row():
			label("Welcome to the Memory Game\nPlease select an option: ")

		with row():
			@button('Normal Mode')
			def normal_play():
				play_game(load_words(extended=False), 3)

			@button('Extended Mode')
			def extended_play():
				play_game(load_words(extended=True), 4)

			@button('Exit')
			def exit():
				w.get().destroy()

if __name__ == "__main__":
#if this is not being imported, i.e) it is being run directly...
	menu()