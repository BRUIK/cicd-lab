# cicd-lab
Library Management System late fee calculator with automated CI/CD pipeline using GitHub Actions

# Library Management System (LMS) - Fine Calculator

A lightweight Python tool that calculates late return fees with daily rates and policy caps.

## How it works
- Late fee = days late × rate per day (Rs. 10/day)
- Fee is capped at a maximum of Rs. 500

## Requirements
Python 3.10+

## How to Run
Run the script using Python:
```bash
python late_fee.py
```

## Running Tests
```bash
pytest
```

## CI/CD
This repo uses GitHub Actions to automatically run tests on every push to `main`. See `.github/workflows/ci.yml`.
