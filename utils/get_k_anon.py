import csv
import sys
from pathlib import Path


def read_from_csv(path: Path) -> list[tuple]:
        """
        Reads CSV file into a list of tuples *including the header*
        """
        with open(path) as csvfile:
                return [tuple(row) for row in csv.reader(csvfile, delimiter=",")]


def compute_k(dataset: list):
	"""
	An anonymity set is the subset of rows in dataset D that share the same QIDs
	D_k satisfies k-anonymity if every anonymity set consists of at least k elements
	"""
	qids = {}

	for row in dataset[1:]:
		key = f"{row[2]}:{row[3]}:{row[4]}"
		qids[key] = qids.get(key, 0) + 1

	return min(qids.values())


def main():
	if len(sys.argv) != 2:
		print(f"Usage: python get_k_anon.py <dataset>")
		sys.exit()

	filepath = Path(sys.argv[1])
	dataset = read_from_csv(filepath)
	k = compute_k(dataset)
	print(f"Dataset {filepath.stem} satisfies {k}-anonymity")


if __name__ == "__main__":
	main()
