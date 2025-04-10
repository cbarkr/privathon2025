# Learning Objectives
By the end of this workshop, you should be able to:
1. Describe (cryptographic) hash functions and their properties
2. Use Hashcat to crack hashes
3. Define k-anonymity, as well as identify its strengths and weaknesses
4. Apply your understanding of hashes to create secure passwords!
# Background
## Hash Functions
> A function that maps data of arbitrary size to fixed-size values
### Properties of Cryptographic Hash Functions
1. Pre-image Resistance: Given the output, it is hard to get the original input (i.e. given $hash(m_1)$, it is hard to find $m_1$)
2. Second Pre-image Resistance: Given one input, it is hard to find another input that produces the same output (i.e. given $m_1$, it is hard to find another $m_2$ such that $m_1 \neq m_2$ and $hash(m_1) = hash(m_2)$)
3. Collision Resistance: Given It is hard to find two inputs that produce the same output (i.e. it is hard to find $m_1$ and $m_2$ such that $m_1 \neq m_2$ and $hash(m_1) = hash(m_2)$)
> [!note]
> Second pre-image resistance and collision resistance differ slightly:
> - Second Pre-image Resistance: Attacker is given a particular message $m_1$
> - Collision Resistance: Attacker can freely choose both messages $m_1$ and $m_2$

## Hashcat
> An open-source hash-cracking tool

See [Tools](#tools)
## K-anonymity
> A property possessed by certain anonymized data
> A release of data is said to have the k-anonymity property if the information for each person contained in the release cannot be distinguished from at least $k − 1$ individuals whose information also appear in the release
### Data Types
1. Identifiers (IDs): A piece of information that uniquely identifies a record (e.g. name, serial number, UUID)
2. Quasi-identifiers (QIDs): Pieces of information that are not of themselves unique identifiers, but are sufficiently well correlated with an entity that they can be combined with other QIDs to create a unique identifier (e.g. gender, birth date, postal code, job title)
3. Sensitive Values: Information that is of interest for research purposes (e.g. disease, salary, interests, political affiliation, transactions)
### Anonymity Set
> The subset of rows in dataset $D$ that share the same **QIDs** (but not necessarily the same sensitive attributes or identifiers)
### Property
> $D_k$ satisfies $k$-anonymity if every anonymity set consists of at least $k$ elements.
### Anonymization Methods
1. Suppression: Remove data outright (e.g. remove column from data or replace data with NULL, etc.); applied to IDs
2. Generalization: Replace individual values of attributes with a broader category (e.g. round integers, broaden location to a larger region); applied to QIDs
### Strengths
1. Can hide QIDs without making the data useless
### Cons
1. Introduces noise to the data
2. May still leak information!
### Attacks
1. Homogeneity Attack: Suppose all members of an anonymity set have the same sensitive value; any person in the anonymity set (i.e. possessing the relevant QIDS) is known to have a certain sensitive value
2. Background Knowledge Attack: Leverages an association between one or more QIDs with the sensitive attribute to reduce the set of possible values for the sensitive attribute
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
## Tasks
### Task 1: Not So Differentially Private
> [!note]
> Names are generated at random from the wordlists, [`first_names.txt`](wordlists/first_names.txt) and [`last_names.txt`](wordlists/last_names.txt), which were obtained from the 2021 Facebook data leak of 533M users
> 
> These wordlists were adapted from [philipperemy's `name-dataset`](https://github.com/philipperemy/name-dataset)

- Suppose that A and B differ by at most one record
- Assume, by some insider knowledge, you happen to learn the name of the last person to be added to the dataset: Joaquim Nuno Chenyi
- [`driver.py`](utils/driver.py) handles parsing the CSV for you
- Who is their vote for?
### Task 2: Hash Cracking
- Suppose we want to identify the name of the youngest individual in the dataset who voted "Red"
- Crack the hashes for their first and last name using Hashcat
- What is their full name?
### Task 3: When Less Is More
- How can you correctly anonymize the dataset?
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
