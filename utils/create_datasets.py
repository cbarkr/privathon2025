import csv
import random
import sys
from hashlib import sha256
from pathlib import Path


NUM_ENTRIES = 1000


def generate_entries(firstnames: Path, lastnames: Path, cities: Path):
	datasetA = []
	datasetB = []

	with open(firstnames) as f:
                first = f.readlines()

        with open(lastnames) as f:
                last = f.readlines()

	with open(cities) as f:
		c = f.readlines()


	for i in range(NUM_ENTRIES+1):
		# IDs
		firstname = sha256(random.choice(first).strip().encode("utf-8")).hexdigest()
		lastname = sha256(random.choice(last).strip().encode("utf-8")).hexdigest()

		# QIDs
		city = random.choice(c).strip()
		age = int(5 * round(random.randint(18, 100) / 5)) # Rounded to nearest 5
		sex = random.choice(["Male", "Female"])

		# Sensitive attributes
		vote = random.choice(["Red", "Blue", "Green", "Orange", "Purple"])

		if i < NUM_ENTRIES:
			datasetA.append((firstname, lastname, city, age, sex, vote))

		# Add an extra entry to datasetB
		datasetB.append((firstname, lastname, city, age, sex, vote))

	# Shuffle the results so the difference isn't trivial
	random.shuffle(datasetA)
	random.shuffle(datasetB)

	return datasetA, datasetB


def write_datasets(datasetA: list, datasetB: list, dest: Path):
	fields = ["H(firstname)", "H(lastname)", "city", "age", "sex", "vote"]

	with open(f"{dest}/A.csv", "w") as csvfile:
		writer = csv.writer(csvfile, delimiter=",")
		writer.writerow(fields)

		for a in datasetA:
			writer.writerow(a)

	with open(f"{dest}/B.csv", "w") as csvfile:
		writer = csv.writer(csvfile, delimiter=",")
		writer.writerow(fields)

		for b in datasetB:
			writer.writerow(b)


def generate_entries_and_write_datasets(firstnames: Path, lastnames: Path, cities: Path, dest: Path):
	datasetA, datasetB = generate_entries(firstnames, lastnames, cities)
	write_datasets(datasetA, datasetB, dest)


def main():
	if len(sys.argv) != 5:
		print(f"Usage: python create_datasets.py <firstnames> <lastnames> <cities> <destination dir>")
		sys.exit()

	firstnames = Path(sys.argv[1])
	lastnames = Path(sys.argv[2])
	cities = Path(sys.argv[3])
	dest = Path(sys.argv[4])

	generate_entries_and_write_datasets(firstnames, lastnames, cities, dest)


if __name__ == "__main__":
	main()
