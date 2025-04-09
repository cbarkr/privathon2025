import csv
import random
import sys
from hashlib import sha256
from pathlib import Path


def generate_entries(firstnames_path: Path, lastnames_path: Path):
	datasetA = []
	datasetB = []

	for i in range(101):
		# IDs
		firstname = sha256(random.choice(open(firstnames_path).readlines()).strip().encode("utf-8")).hexdigest()
		lastname = sha256(random.choice(open(lastnames_path).readlines()).strip().encode("utf-8")).hexdigest()

		# QIDs
		age = int(5 * round(random.randint(18, 100) / 5)) # Rounded to nearest 5
		sex = random.choice(["Male", "Female"])

		# Sensitive attributes
		vote = random.choice(["Red", "Blue", "Green", "Orange", "Purple"])

		if i < 100:
			datasetA.append((firstname, lastname, age, sex, vote))

		# Add an extra entry to datasetB
		datasetB.append((firstname, lastname, age, sex, vote))

	# Shuffle the results so the difference isn't trivial
	random.shuffle(datasetA)
	random.shuffle(datasetB)

	return datasetA, datasetB


def write_datasets(datasetA: list, datasetB: list, dest_dir_path: Path):
	fields = ["H(firstname)", "H(lastname)", "age", "sex", "vote"]

	with open(f"{dest_dir_path}/datasetA.csv", "w") as csvfile:
		writer = csv.writer(csvfile, delimiter=",")
		writer.writerow(fields)

		for a in datasetA:
			writer.writerow(a)

	with open(f"{dest_dir_path}/datasetB.csv", "w") as csvfile:
		writer = csv.writer(csvfile, delimiter=",")
		writer.writerow(fields)

		for b in datasetB:
			writer.writerow(b)


def generate_entries_and_write_datasets(firstnames_path: Path, lastnames_path: Path, dest_dir_path: Path):
	datasetA, datasetB = generate_entries(firstnames_path, lastnames_path)
	write_datasets(datasetA, datasetB, dest_dir_path)


def main():
	if len(sys.argv) != 4:
		print(f"Usage: python create_datasets.py <firstnames> <lastnames> <destination dir>")
		sys.exit()

	firstnames_path = Path(sys.argv[1])
	lastnames_path = Path(sys.argv[2])
	dest_dir_path = Path(sys.argv[3])

	generate_entries_and_write_datasets(firstnames_path, lastnames_path, dest_dir_path)


if __name__ == "__main__":
	main()
