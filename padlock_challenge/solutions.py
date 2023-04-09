""" PADLOCK CHALLENGE SOLUTION MODULE """


def challenge1():
	""" Solution to challenge 1 """
	#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-1/

	print(f"Challenge 1 Code: {sum(list(range(41)))}")


def challenge2():
	""" Solution to challenge 2 """
	# Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/

	code = 0
	for digit1 in range(8):
		for digit2 in range(1,9):
			for digit3 in range(2,10):
				if digit1 < digit2 < digit3:
					code += 1

	print(f"Challenge 2 Code: {code}")

def challenge3():
	""" Solution to challenge 3 """
	#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-3/

	code = 0
	for digit1 in range(0, 10, 2):
		for digit2 in range(0, 10, 2):
			for digit3 in range(0, 10, 2):
				code += 1

	print(f"Challenge 3 Code: {code}")

def challenge4():
	""" Solution to challenge 4 """
	#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-4/

	code = 0
	for digit1 in range(0, 10):
		for digit2 in range(0, 10):
			for digit3 in range(0, 10):
				sum = (digit1 + digit2 + digit3) % 2
				if sum:
					code += 1
	print(f"Challenge 4 Code: {code}")
		
def challenge5():
	""" Solution to challenge 5 """
	#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-4=5/

	code = 0
	for digit1 in range(10):
		for digit2 in range(10):
			for digit3 in range(10):
				if digit1 == digit2 or digit2 == digit3 or digit3 == digit1:
					code += 1

	print(f"Challenge 5 Code: {code}")

if __name__ == '__main__':
    challenge1()
    challenge2()
    challenge3()
    challenge4()
    challenge5()
