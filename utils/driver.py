import sys
import csv
from pathlib import Path


def read_from_csv(path: Path) -> list[tuple]:
	"""
	Reads CSV file into a list of tuples *including the header*
	"""
	with open(path) as csvfile:
		return [tuple(row) for row in csv.reader(csvfile, delimiter=",")]


def read_datasets(datasetA: Path, datasetB: Path) -> tuple:
	A = read_from_csv(datasetA)
	B = read_from_csv(datasetB)

	return A, B


def difference_attack(A: list, B: list) -> set:
	"""
	Task 1: Not So Differentially Private

	- Suppose that A and B differ by at most one record
	- Assume, by some insider knowledge, you happen to learn the name of the *last* person to be added
	- Who is their vote for?
	"""
	# TODO: Implement!
	...


def hash_crack(A: list, B: list) -> tuple[str, str]:
	"""
	Task 2: Hash Cracking

	- Suppose we want to identify the name of the youngest individual in the dataset who voted "Red"
	- Use this function to find the relevant record
	- Then crack the hashes for their first and last name using Hashcat
	- What is their full name?
	- Return the hashes as the tuple (firstname, lastname)
	"""
	# TODO: Implement!
	...


def anonymize(A: list, B: list) -> list:
	"""
	Task 3: When Less Is More

	- We've seen that hashing doesn't work for suppressing data
	- How can you correctly anonymize the dataset?
	- Return the anonymized version of the largest dataset
	"""
	# TODO: Implement!


def main():
	if len(sys.argv) != 3:
		print(f"Usage: python driver.py <dataset A> <dataset B>")
		sys.exit()

	datasetA = Path(sys.argv[1])
	datasetB = Path(sys.argv[2])

	A, B = read_datasets(datasetA, datasetB)

	task1 = difference_attack(A, B)
	print(f"task 1: {task1}")

	task2 = hash_crack(A, B)
	print(f"task 2: {task2}")

	task3 = anonymize(A, B)
	print(f"task 3: {task3}")


if __name__ == "__main__":
	main()
