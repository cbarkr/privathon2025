import sys
import csv
from pathlib import Path


def read_from_csv(path: Path) -> list[tuple]:
	"""
	Reads CSV file into a list of tuples *including the header*
	"""
	with open(path) as csvfile:
		return [tuple(row) for row in csv.reader(csvfile, delimiter=",")]


def read_datasets(datasetA: Path, datasetB: Path, datasetC: Path) -> tuple:
        A = read_from_csv(datasetA)
        B = read_from_csv(datasetB)
        C = read_from_csv(datasetC)

        return A, B, C


def task1(A: list, B: list) -> str:
	"""
	Task 1: Background Knowledge / Differencing Attack

	- Suppose that A and B differ by at most one record
	- Assume, by some insider knowledge, you happen to learn the name of the *last* person to be added
	- Who is their vote for? Return the vote as a string
	"""
	# TODO: Implement!
	...


def task2(B: list) -> str:
	"""
	Task 2: Homogeneity Attack

	- Suppose you know a woman from Burnaby who is included in the dataset
	- Who is her vote for? Return the vote as a string
	"""
	# TODO: Implement!
	...


def task3(B: list) -> tuple[str, str]:
	"""
	Task 3: Hash Cracking

	- Suppose we want to identify the name of the youngest individual in the dataset who voted "Red"
	- Return the hashes of their first and last name as a tuple (firstname, lastname)
	- Then, crack the hashes using Hashcat and the name wordlists in `wordlists`
	"""
	# TODO: Implement!
	...


def task4(passwords: list) -> str:
	"""
	Task 4: Password Cracking

	- Suppose that the individual from task 3 was involved in a data breach by the social media site Fakebook, leaking names and PBKDF2-hashed passwords
	- Fakebook's password "strength" requirements dictate that passwords must be at least 10 characters and contain at least one number and special character
	- Also suppose that the individual, like most people, meets only the minimum password requirements in a predictable way: <word><number><special-characte>
	- Return the individual's password hash as a string
	- Then, crack the hash using Hashcat and the password wordlist (`rockyou.txt`) in `wordlists`
	"""
	# TODO: Implement!
	...


def task5(B: list) -> list:
	"""
	Task 5: Anonymization

	- We've seen that hashing doesn't work for suppressing data
	- How can you correctly anonymize the dataset?
	- Return the anonymized version of the largest dataset
	"""
	# TODO: Implement!


def main():
	if len(sys.argv) != 4:
		print(f"Usage: python driver.py <dataset A> <dataset B> <password dataset>")
		sys.exit()

	A, B, passwords = read_datasets(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))

	task1 = task1(A, B)
	print(f"task 1: {task1}")

	task2 = task2(B)
	print(f"task 2: {task2}")

	task3 = task3(B)
	print(f"task 3: {task3}")

	task4 = task4(passwords)
	print(f"task 4: {task4}")

	task5 = task5(B)
	print(f"task 5: {task5}")


if __name__ == "__main__":
	main()
