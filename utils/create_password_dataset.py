import csv
import os
import random
import sys
from base64 import b64encode
from string import digits, punctuation
from hashlib import pbkdf2_hmac
from pathlib import Path

NUM_ENTRIES = 10000


def generate_entries(firstnames: Path, lastnames: Path, rockyou: Path):
    dataset = []

    with open(firstnames) as f:
        first = f.readlines()

    with open(lastnames) as f:
        last = f.readlines()

    with open(rockyou) as f:
        passwords = f.readlines()

    for i in range(NUM_ENTRIES):
        firstname = random.choice(first).strip()
        lastname = random.choice(last).strip()

        pw_base = random.choice(passwords).strip()
        pw_num_part = "".join(
            [random.choice(digits) for _ in range(random.randint(1, 4))]
        )
        pw_special_part = "".join(
            [random.choice(punctuation) for _ in range(random.randint(1, 4))]
        )

        password = pw_base + pw_num_part + pw_special_part

        algo = "sha256"
        salt = os.urandom(16)
        iters = 1000
        hashed_password = pbkdf2_hmac(algo, password.encode("utf-8"), salt, iters)

        formatted_password = f"{algo}:{iters}:{b64encode(salt).decode('utf-8')}:{b64encode(hashed_password).decode('utf-8')}"

        dataset.append((firstname, lastname, formatted_password))

    return dataset


def write_dataset(dataset: list, dest: Path):
    fields = ["firstname", "lastname", "password"]

    with open(f"{dest}/passwords.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(fields)

        for row in dataset:
            writer.writerow(row)


def generate_entries_and_write_dataset(
    firstnames: Path, lastnames: Path, rockyou: Path, dest: Path
):
    dataset = generate_entries(firstnames, lastnames, rockyou)
    write_dataset(dataset, dest)


def main():
    if len(sys.argv) != 5:
        print(
            f"Usage: python create_password_dataset.py <firstnames> <lastnames> <rockyou> <destination-dir>"
        )
        sys.exit()

    firstnames = Path(sys.argv[1])
    lastnames = Path(sys.argv[2])
    rockyou = Path(sys.argv[3])
    dest = Path(sys.argv[4])

    generate_entries_and_write_dataset(firstnames, lastnames, rockyou, dest)


if __name__ == "__main__":
    main()
