# Scenario
- Suppose that a small marketing firm (let's call them "Oxford Analytica") has collected data on political affiliations
- For each record, they store the following information:
	1. First name
	2. Last name
	3. Age
	4. Sex
	5. Vote
- Oxford Analytica supposedly cares about privacy, and they've heard about [k-anonymity](https://en.wikipedia.org/wiki/K-anonymity), so they try to anonymize the data like so:
	1. Suppress identifiers (first name, last name) by hashing them with SHA-256
	2. Generalize quasi-identifiers (age) by rounding to the nearest 5
	3. Leaving the sensitive information (vote) untouched since this is necessary for their analysis
- Further suppose that you are a data analyst who has obtained 2 sequential releases of the data, A and B
## Tasks
### Task 1: Not So Differentially Private
> [!note]
> Names are generated at random from the wordlists, [`first_names.txt`](wordlists/first_names.txt) and [`last_names.txt`](wordlists/last_names.txt), which were obtained from the 2021 Facebook data leak of 533M users
> 
> These wordlists were adapted from [philipperemy's `name-dataset`](https://github.com/philipperemy/name-dataset)

- Assume, by some insider knowledge, you happen to learn the name of the last person to be added to the dataset: Bouhala الصول
- [`driver.py`](utils/driver.py) handles parsing the CSV for you
- Who is their vote for?
### Task 2: Hash Cracking
- Suppose we want to identify the name of the youngest individual in the dataset who voted "Red"
- Crack the hashes for their first and last name using Hashcat
- What is their full name?

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
