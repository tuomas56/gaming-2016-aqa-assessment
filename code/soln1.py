from sguigee import *
import random

def load_words(extended=False):
	with open("WordsExt.txt" if extended else "Words.txt") as f:
		return list(map(str.strip, f.read().split("\n")))[:-1]

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def draw_grid(words, c, n):
	PADDING = (10, 10)
	offset_x = (50*len(words)/n - PADDING[0] * (n - 1)) / 2
	offset_y = (20*len(words)/n - PADDING[1] * (n - 1)) / 2
	START = (200 - offset_x, 200 - offset_y)
	for i, x in enumerate(chunks(words, n)):
		for j, t in enumerate(x):
			c.create_text((START[0] + j*50 + j*PADDING[0], START[1] + i*20 + i*PADDING[1]), text=t)

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
				nonlocal words
				random.shuffle(words)
				words, to_replace = words[:-1], words[-1]
				draw_grid(words, c, size)
				@after(30)
				def then():
					words[-1], replaced = to_replace, words[-1]
					random.shuffle(words)
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
	for i in range(guesses, 0, -1):
		guess = ask_message(prompt % i)
		if guess == word:
			return True
	return False

def end_game(c, removed, replaced):
	c.clear()
	if removed is True:
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
	menu()