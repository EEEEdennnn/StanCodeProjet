"""
File: coin_flip_runs.py
Name:Eden
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO:
	"""
	print("Let's flip a coin!")
	number = int(input('Number of runs: '))
	n1 = ""
	roll1 = r.randrange(1, 3)
	n1 += str(roll1)
	run = 0
	can_add = True
	while True:
		roll2 = r.randrange(1,3)
		n1 += str(roll2)
		if roll1 == roll2:
			if can_add:
				run += 1
				can_add = False
		else:
			can_add = True
		roll1 = roll2
		if run == number:
			print_out_n1(n1)
			break


def print_out_n1(n1):
	ans = ''
	for ch in n1:
		if ch == '1':
			ans += 'H'
		else:
			ans += 'T'
	print(ans)




# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
