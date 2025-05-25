import sys
import csv
from pathlib import Path


################
# START: Utils #
################


def read_from_csv(path: Path) -> list[tuple]:
    """
    Reads CSV file into a list of tuples *including the header*
    """
    with open(path, encoding="utf-8") as csvfile:
        return [tuple(row) for row in csv.reader(csvfile, delimiter=",")]


def read_datasets(datasetA: Path, datasetB: Path, datasetC: Path) -> tuple:
    A = read_from_csv(datasetA)
    B = read_from_csv(datasetB)
    C = read_from_csv(datasetC)

    return A, B, C


def write_dataset(dataset: list, dest: Path):
    with open(dest, "w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")

        for row in dataset:
            writer.writerow(row)


##############
# END: Utils #
##############


################
# START: Tasks #
################


def task1(A: list, B: list) -> str:
    """
    Task 1: Background Knowledge / Differencing Attack

    - Suppose that A and B differ by at most one record
    - Assume, by some insider knowledge, you happen to learn the name of the *last* person to be added
    - Who is their vote for? Return the vote as a string
    """
    return set(B).difference(set(A)).pop()[-1]


def task2(B: list) -> str:
    """
    Task 2: Homogeneity Attack

    - Suppose you know a female from Burnaby who is included in the dataset
    - Who is their vote for? Return the vote as a string
    """
    return [i[5] for i in B if i[2] == "Burnaby" and i[4] == "Female"][0]


def task3(B: list) -> tuple[str, str]:
    """
    Task 3: Hash Cracking

    - Suppose we want to identify the name of the youngest female in the dataset who voted "Red"
    - Return the hashes of their first and last name as a tuple (firstname, lastname)
    - Then, crack the hashes using Hashcat and the name wordlists in `wordlists`
    """
    curr = []
    youngest = 100
    for i in B[1:]:
        if int(i[3]) < youngest and i[4] == "Female" and i[5] == "Red":
            youngest = int(i[3])
            curr = i

    return (curr[0], curr[1])


def task4(passwords: list) -> str:
    """
    Task 4: Password Cracking

    - Suppose that the individual from task 3 was involved in a data breach by the social media site Fakebook, leaking names and PBKDF2-hashed passwords
    - Fakebook's password "strength" requirements dictate that passwords must be at least 10 characters and contain at least one number and special character
    - Also suppose that the individual, like most people, meets only the minimum password requirements in a predictable way: <word><number><special-characte>
    - Return the individual's password hash as a string
    - Then, crack the hash using Hashcat and the password wordlist (`rockyou.txt`) in `wordlists`
    """
    # NOTE: Obtained from result of task3
    firstname = "Esme"
    lastname = "Lavigne"
    hash = ""

    for i in passwords[1:]:
        if i[0] == firstname and i[1] == lastname:
            hash = i[2]
            break

    return hash


def task5(B: list) -> list:
    """
    Task 5: Anonymization

    - We've seen that hashing doesn't work for suppressing data
    - How can you correctly anonymize the dataset?
    - Return the anonymized version of the dataset
    """
    from collections import Counter

    # NOTE: k chosen arbitrarily
    k = 2
    anonymized = [B[0]]
    anonymity_sets = Counter()
    anonymity_sets_backlog: dict[tuple, list] = {}

    # First pass: Find and better suppress/generalize data in anonymity sets
    for i in B[1:]:
        # Round age to nearest 10
        rounded_age = int(10 * round(int(i[3]) / 10))

        # Suppress name (hashes) and round age
        new_i = ("********", "********", i[2], rounded_age, *i[4:])

        # Generate key from (City, Age, Sex) 3-tuple
        key = new_i[2:5]

        # Increment size of anonymity set
        anonymity_sets[key] += 1

        # Backlog for this anonymity set doesn't exist yet
        if not anonymity_sets_backlog.get(key):
            # Let's create a new list for this
            anonymity_sets_backlog[key] = [new_i]
        
        # Backlog exists
        else:
            # Add to it
            anonymity_sets_backlog[key].append(new_i)

    # Second pass: Add anonymity sets with size >= k to dataset
    for key, count in anonymity_sets.items():
        if count >= k:
            backlog = anonymity_sets_backlog[key]

            for b in backlog:
                anonymized.append(b)

    return anonymized


##############
# END: Tasks #
##############


def main():
    if len(sys.argv) != 4:
        print(f"Usage: python driver.py <dataset A> <dataset B> <password dataset>")
        sys.exit()

    A, B, passwords = read_datasets(
        Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    )

    task1_res = task1(A, B)
    print(f"task 1: {task1_res}")

    task2_res = task2(B)
    print(f"task 2: {task2_res}")

    task3_res = task3(B)
    print(f"task 3: {task3_res}")

    task4_res = task4(passwords)
    print(f"task 4: {task4_res}")

    task5_res = task5(B)
    write_dataset(task5_res, Path("./task5.csv"))
    print(f"task 5: Results written to 'task5.csv'")


if __name__ == "__main__":
    main()
