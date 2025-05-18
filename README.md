# Table of Contents
1. [Tools](#tools)
2. [Scenario](#scenario)
3. [Tasks](#tasks)
4. [Credits](#credits)

---
# Tools
- [Hashcat](https://hashcat.net/hashcat/)
## Install
### Windows

| Step | Program | Install Link                                          |
| ---- | ------- | ----------------------------------------------------- |
| 1    | 7zip    | [install](https://www.7-zip.org/a/7z2409-x64.exe)     |
| 2    | hashcat | [install](https://hashcat.net/files/hashcat-6.2.6.7z) |
### Mac
#### Method 1: Homebrew
```bash
brew install hashcat
```
#### Method 2: Executable Installers

| Step | Program | Install Link                                          |
| ---- | ------- | ----------------------------------------------------- |
| 1    | 7zip    | [install](https://7-zip.org/a/7z2409-mac.tar.xz)      |
| 2    | hashcat | [install](https://hashcat.net/files/hashcat-6.2.6.7z) |
### Linux
#### Ubuntu/Debian/Mint
```bash
sudo apt install hashcat
```
#### Fedora/RHEL
```bash
sudo dnf install hashcat
```
#### Arch
If you use Arch (btw), you don't need me to tell you

---
# Scenario
- Suppose that a small marketing firm (let's call them "Oxford Analytica") has collected data on political affiliations
- For each record, they store the following information:
	1. First name
	2. Last name
	3. City
	4. Age
	5. Sex
	6. Vote
- In their analysis, they hope to find a correlation between age, sex, city, and vote
- Oxford Analytica supposedly cares about privacy, and they've heard about [k-anonymity](https://en.wikipedia.org/wiki/K-anonymity), so they try to anonymize the data like so:
	1. Suppress identifiers (first name, last name) by hashing them with SHA-256
	2. Generalize quasi-identifiers (age) by rounding to the nearest 5
	3. Leaving the sensitive information (vote) untouched since this is necessary for their analysis
- Further suppose that you are a data analyst who has obtained 2 sequential releases of the data, [A](datasets/A.csv) and [B](datasets/B.csv)

---
# Tasks
- Write all solutions in [`driver.py`](utils/driver.py)
	- This script handles parsing the datasets and other setup for you!!!
## Task 1: Background Knowledge / Differencing Attack
- Suppose that A and B differ by at most one record
- Assume, by some insider knowledge, you happen to learn the name of the last person to be added to the dataset: Joaquim Nuno Chenyi
- Who is their vote for?
## Task 2: Homogeneity Attack
- Suppose you know a female from Burnaby who is included in the dataset
- Who is their vote for?
## Task 3: Hash Cracking
- Suppose we want to identify the name of the youngest female in the dataset who voted "Red"
- Crack the hashes for their first and last name using Hashcat
- What is their full name?
## Task 4: Password Cracking
> [!note]
> Hashcat's [hybrid attack](https://hashcat.net/wiki/doku.php?id=hybrid_attack) and [mask attack](https://hashcat.net/wiki/doku.php?id=mask_attack) docs may or may not be of some use to you

- Suppose that the individual from task 3 was involved in a data breach by the social media site "Fakebook", leaking names and passwords hashed with  PBKDF2-HMAC-SHA256
- Fakebook's password "strength" requirements dictate that passwords must be at least 10 characters and contain at least one number and special character
- Also suppose that the individual, like most people, meets only the minimum password requirements in a predictable way: `<word><number(s)><special-character>`
- Using [`rockyou.txt`](wordlists/rockyou.txt) (a common password wordlist) and Hashcat, crack the password
- What is their password in plaintext?
## Task 5: Anonymization
- How can you correctly anonymize the dataset?

---
# Credits
- Name wordlists ([`first_names.txt`](wordlists/first_names.txt) and [`last_names.txt`](wordlists/last_names.txt)): Adapted from [philipperemy's `name-dataset`](https://github.com/philipperemy/name-dataset), which was obtained from the 2021 Facebook data leak of 533M users
- Cities wordlist ([`canadian_cities.txt`](wordlists/canadian_cities.txt)): Adapted from [Wikipedia](https://en.wikipedia.org/wiki/List_of_cities_in_Canada)
- RockYou wordlist ([`rockyou.txt`](wordlists/rockyou.txt)): Adapted from [Weakpass](https://weakpass.com/wordlists/rockyou.txt), obtained from the 2009 RockYou data breach of 32M plaintext passwords
