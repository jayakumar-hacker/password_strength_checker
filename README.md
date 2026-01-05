# Password Strength Checker

A Python-based password strength checker focused on preventing weak,
predictable passwords that are vulnerable to brute-force and dictionary
attacks. This project is built for developers and students who want a
practical, real-world approach to password validation.

The tool evaluates passwords using user-specific data and known exposed
password patterns, ensuring stronger security before passwords are used
in applications.

---

## Overview

Password Strength Checker validates a password by analyzing personal
information usage, common password exposure, and structural weaknesses.
It blocks unsafe passwords early and assigns a strength score for safer
password selection.

---

## Key Features

- Prevents passwords containing user personal data
- Detects globally exposed passwords
- Includes Indian common words (Tamil base words)
- Identifies keyboard patterns and sequences
- Rule-based password strength scoring
- CLI-based implementation
- No external dependencies

---

## How It Works

1. User provides password, name, date of birth, phone number, and email.
2. Password is checked against user-specific data.
3. Password is compared with `common_passwords.txt`, containing global
   and Indian weak base words.
4. Hard rule matches mark the password unsafe immediately.
5. Soft rules analyze length, character diversity, repetition, and
   sequences.
6. A strength score from 0 to 100 is calculated.

---

## Why a Password is Weak

This project not only checks password strength but also explains why a password is considered weak.  

Currently, the password is flagged as weak for the following reasons:

- Too short (less than 8 characters)
- Contains only letters or only digits
- Matches common patterns (like '12345', 'password')
- Contains repeated sequences (like 'aaa' or '111')
- Contains personal or common words (like names or common Tamil words)

The program prints these reasons to help users improve their passwords.

---

## Requirements

- Python 3.8 or higher
- No third-party libraries

---

## Installation

```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker
```
---

## Usage

```bash
python main.py
```
---

## Project Structure

password_strength_checker/
│
├── main.py                 # CLI input and output
├── checker.py              # Password validation and scoring
├── rules.py                # Core password rules
├── common_passwords.txt    # Global + Indian weak passwords
├── README.md

---

## Limitations

- Basic validation for personal inputs
- CLI-only interface

---

## Future Plans

- Improved validation logic
- GUI interface
- PyPI package release
- Advanced security rule expansion

---

## License

- MIT License

---

## Author
- Jayakumar K
- Github-link : https://github.com/jayakumar-hacker/password_strength_checker/
- 

--- 

