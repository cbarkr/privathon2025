import sys
import csv
from pathlib import Path


def read_from_csv(firstnames_path: Path, lastnames_path: Path):
	datasetA = []
	datasetB = []

	with open(firstnames_path) as csvfile:
		reader = csv.reader(csvfile, delimiter=",")
		for idx, row in enumerate(reader):
			if idx > 0:
				datasetA.append(tuple(row))

	with open(lastnames_path) as csvfile:
		reader = csv.reader(csvfile, delimiter=",")
		for idx, row in enumerate(reader):
			if idx > 0:
				datasetB.append(tuple(row))

	return datasetA, datasetB


def difference_attack(datasetA: list, datasetB: list):
	"""
	Attack 1: Set differencing

	Suppose datasetA and datasetB differ by only record
	Also suppose you know the name of the *last* person to be added
	What is the vote of the identified user?
	"""

	# TODO: Implement!
	...


def main():
	if len(sys.argv) != 3:
		print(f"Usage: python create_datasets.py <firstnames> <lastnames>")
		sys.exit()

	firstnames_path = Path(sys.argv[1])
	lastnames_path = Path(sys.argv[2])

	datasetA, datasetB = read_from_csv(firstnames_path, lastnames_path)

	difference_attack(datasetA, datasetB)


if __name__ == "__main__":
	main()
