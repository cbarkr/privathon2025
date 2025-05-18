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
    with open(path) as csvfile:
        return [tuple(row) for row in csv.reader(csvfile, delimiter=",")]


def read_datasets(datasetA: Path, datasetB: Path, datasetC: Path) -> tuple:
    A = read_from_csv(datasetA)
    B = read_from_csv(datasetB)
    C = read_from_csv(datasetC)

    return A, B, C


def write_dataset(dataset: list, dest: Path):
    with open(dest, "w") as csvfile:
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
    # TODO: Implement!
    ...


def task2(B: list) -> str:
    """
    Task 2: Homogeneity Attack

    - Suppose you know a female from Burnaby who is included in the dataset
    - Who is their vote for? Return the vote as a string
    """
    # TODO: Implement!
    ...


def task3(B: list) -> tuple[str, str]:
    """
    Task 3: Hash Cracking

    - Suppose we want to identify the name of the youngest female in the dataset who voted "Red"
    - Return the hashes of their first and last name as a tuple (firstname, lastname)
    - Then, crack the hashes using Hashcat and the name wordlists in `wordlists`
    """
    # TODO: Implement!
    ...


def task4(passwords: list) -> str:
    """
    Task 4: Password Cracking

    - Suppose that the individual from task 3 was involved in a data breach by the social media site Fakebook, leaking names and passwords hashed with PBKDF2-HMAC-SHA256
    - Fakebook's password "strength" requirements dictate that passwords must be at least 10 characters and contain at least one number and one special character
    - Also suppose that the individual, like most people, meets only the minimum password requirements in a predictable way: <word><number><special-character>
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
    print(f"task 5: {task5_res}")

    write_dataset(task5_res, Path("./task5.csv"))


if __name__ == "__main__":
    main()
