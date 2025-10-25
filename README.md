# password-strength-analyzer
Simple Python CLI password strength analyzer — checks length, character variety, and common weak passwords.

# Password Strength Analyzer (CLI)

Simple Python CLI tool that rates password strength based on length, character variety, and common weak passwords.

## Features
- Checks length, upper/lowercase, digits, and symbols
- Detects common weak passwords and common words
- Produces a score and actionable advice
- Optional colored output with `colorama`

## Usage
```bash
# optional: create venv
python -m venv venv
source venv/bin/activate   # linux/mac
venv\Scripts\activate      # windows

# install colorama if you want colored output
pip install colorama

# run
python password_checker.py

# optionally supply a custom common-passwords file
python password_checker.py common_passwords.txt
