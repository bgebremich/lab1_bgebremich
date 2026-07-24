# Grade Evaluator

A Python tool that takes a student's assignment scores from a CSV file and works out their final grade, GPA, and whether they passed or failed.

## What it does

You give it a CSV file with your assignments, scores, and weights, and it:
- Checks all the data is valid before doing anything
- Calculates your weighted final grade and GPA (out of 5.0)
- Tells you if you passed or failed Formative and Summative separately (you need 50%+ in both)
- If you failed any formative assignments, it tells you which one(s) to resubmit based on highest weight

## Files in this repo

- `grade-evaluator.py` — the main script that does all the work
- `organizer.sh` — a shell script that backs up your CSV, creates a fresh one, and keeps a log
- `grades.csv` — the input file with assignment data
- `README.md` — you're reading it

## How to run it

**Directly with Python:**
```bash
python grade-evaluator.py
```
It will ask you for the filename — just type `grades.csv` and hit Enter.

**Or use the shell script:**
```bash
bash organizer.sh
```
This automatically backs up the old grades.csv with a timestamp, creates a fresh one, runs the evaluator, and logs everything to `organizer.log`.

## CSV structure

Your CSV needs these four columns:# grade-evaluator


A few rules:
- `group` has to be either `Formative` or `Summative`
- `score` must be a number between 0 and 100
- Formative weights must add up to 60, Summative to 40, and the total must be 100

## GPA calculation

`GPA = (Final Grade / 100) x 5.0`

Pass/Fail is checked per category — so even if your overall average looks okay, you still need at least 50% in both Formative and Summative independently.

## Error handling

The script won't crash on bad input. It catches things like:
- File not found
- Empty or blank rows
- Scores outside the 0–100 range
- Wrong group names
- Weights that don't add up correctly
- Missing columns in the CSV

