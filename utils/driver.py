import sys
import csv
from pathlib import Path


def read_from_csv(datasetA: Path, datasetB: Path):
	with open(datasetA) as csvfile:
		A = [tuple(row) for row in csv.reader(csvfile, delimiter=",")]

	with open(datasetB) as csvfile:
		B = [tuple(row) for row in csv.reader(csvfile, delimiter=",")]

	return A, B


def difference_attack(A: list, B: list):
	"""
	Attack 1: Set differencing

	Suppose dataset A and dataset B differ by only record
	Also suppose you know the name of the *last* person to be added
	What is the vote of the identified user?
	"""

	# TODO: Implement!
	...


def main():
	if len(sys.argv) != 3:
		print(f"Usage: python driver.py <dataset A> <dataset B>")
		sys.exit()

	datasetA = Path(sys.argv[1])
	datasetB = Path(sys.argv[2])

	A, B = read_from_csv(datasetA, datasetB)

	difference_attack(A, B)


if __name__ == "__main__":
	main()
