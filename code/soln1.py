from sguigee import *
import random

def load_words(extended=False):
	with open("WordsExt.txt" if extended else "Words.txt") as f:
		return list(map(str.strip, f.read().split("\n")))

def chunks(l, n):
#split a list into evenly sized chunks.
    for i in range(0, len(l), n):
        #iterate with a step of n
        yield l[i:i+n]
        #yield a block of length n

def draw_grid(words, c, n):
	START = (40, 80)
	PADDING = (10, 10)
	for i, x in enumerate(chunks(words, n)):
		for j, t in enumerate(x):
			c.create_text((START[0] + j*50 + j*PADDING[0], START[1] + i*10 + i*PADDING[1]), text=t)

def play_game(words, size):
	with window(title="Memory Game") as w:
		with row():
			c = canvas(width=200, height=200)
			c.create_text((100, 100), text="Press 'Start' to start.")

		with row() as r:
			@button("Start")
			def start():
				c.clear()
				r.destroy()
				nonlocal words
				random.shuffle(words)
				words, to_replace = words[:-1], words[-1]
				draw_grid(words, c, size)
				@after(3)
				def then():
					words[-1], replaced = to_replace, words[-1]
					random.shuffle(words)
					c.clear()
					draw_grid(words, c, size)
					for _ in range(3):
						if ask_word(removed=True):
							break
					with row() as r1:
						rml = label("What word was removed?")

					with row() as r2:
						rm = textbox()

					with row() as r3:
						rpl = label("What word was it replaced with?")

					with row() as r4:
						rp = textbox()

					with row() as r5:
						@button('Check')
						def check():
							c.clear()
							r1.destroy()
							r2.destroy()
							r3.destroy()
							r4.destroy()
							r5.destroy()
							if to_replace == rp.get() and replaced == rm.get():
								c.create_text((100, 50), text='Well Done!')
							else:
								c.create_text((100, 50), text='Not quite.')
								c.create_text((110, 90), text='The actual word\nremoved was %s.' % replaced)
								c.create_text((100, 130), text='And it was replaced\nwith %s.' % to_replace)

							with row():
								@button('Done')
								def done():
									w.get().destroy()



def menu():
	with window('Menu') as w:
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