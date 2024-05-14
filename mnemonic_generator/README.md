# Mnemonic Phrase Generator

This Python script generates BIP 39 compatible mnemonic phrases and optionally saves them to a file. Mnemonic phrases are useful for securely deriving cryptographic keys, such as those used in cryptocurrency wallets.

## Features

- Generate one or more BIP 39 compatible mnemonic phrases.
- Specify the number of phrases and the number of words per phrase.
- Save generated phrases to a text file for future use.
- Customize output with ANSI color formatting for improved readability.

## Installation

1. Ensure you have Python 3 installed on your system.
2. Clone this repository or download the `mnemonic_generator.py` script.
3. Install required dependencies using pip:

   ```bash
   pip install mnemonic colorama


# Usage


### Command-line Options

Run the script using the command-line interface (CLI) with the following options:

- `-p, --phrases N`: Specify the number of mnemonic phrases to generate (default: 1).
- `-w, --words {12,15,18,21,24}`: Specify the number of words per phrase (choices: 12, 15, 18, 21, 24; default: 12).
- `-o, --output FILE`: Save generated phrases to the specified output file.


### Examples

#### Generate and Save to File

Generate a single mnemonic phrase with 24 words and save it to a file named `output.txt`:

```bash
python mnemonic_generator.py -p 1 -w 24 -o output.txt


### Examples

#### Generate and Save to File

Generate a single mnemonic phrase with 24 words and save it to a file named `output.txt`:

```bash
python mnemonic_generator.py -p 1 -w 24 -o output.txt
