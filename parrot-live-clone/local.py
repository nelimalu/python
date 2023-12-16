from os import system as sys
from random import choice
import signal
from time import sleep


def exit(signal, frame):
	sys('cls')
	sys("color 0f")
	sys.exit(0)


colours = "1 2 3 4 5 6 7 8 9 0 a b c d e f".split()
frames = []
for i in range(10):
	with open(f"./frames/{i}.txt", 'r') as file:
		frames.append(file.read())


def main():

	counter = 0
	while True:
		sys("cls")
		sys(f"color 0{choice(colours)}")
		print(frames[counter])

		counter += 1
		counter %= len(frames)
		sleep(0.05)


if __name__ == "__main__":
	signal.signal(signal.SIGINT, exit)
	main()
