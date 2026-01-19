# Ask Paragraf, change what to what

def main():
	word = ""

	try:
		n_word_2_chge = int(input("How many word do you want to change (n):\n"))
	except TypeError:
		print("You type wrong, changing your word to 1")
		n_word_2_chge = 1
	for word in range(n_word_2_chge):
		wordchge = []
		word = input(f"({word + 1}) word you want to change: ")
		wordchge.append(word)
	for wordch in range(n_word_2_chge):
		word2chge = []
		word = input(f"({word+1}) word to change: ")
		word2chge.append(word)

	lowcaps = input("Would you want to remove capitalization? (Y/n) ")
	lowcaps = lowcaps.upper()
	if lowcaps == "Y":
		for w in wordchge:
			wordcghe[w].lower() 
	elif lowcaps == "N":
		for w in word2chge:
			word2chge[w].lower()

def changer(p, w, w2c):
	#paragraf, word, word 2 change
	for word in p:
		for w_chge in w:
			if word == w_chge:
				p[word] == w2c[w_chge]

if __name__ == "__main__":
	main()