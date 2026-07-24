import csv
import sys

def load_csv_data(filename):
    data = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Skip empty or whitespace-only rows
                if not row or not any(row.values()):
                    continue
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    return data

def validate_and_evaluate(data):
    if not data:
        print("Error: The CSV file is empty or contains no valid data rows.")
        return

    formative_score = 0.0
    formative_weight = 0.0
    summative_score = 0.0
    summative_weight = 0.0

    failed_formatives = []

    for idx, row in enumerate(data, start=1):
        # Check for missing columns
        if not all(k in row for k in ('assignment', 'score', 'weight', 'group')):
            print(f"Error: Row {idx} is missing required columns.")
            return

        try:
            score = float(row['score'])
            weight = float(row['weight'])
        except (ValueError, TypeError):
            print(f"Error: Row {idx} has non-numeric score or weight values.")
            return

        # Score range validation
        if not (0 <= score <= 100):
            print(f"Error: Score in row {idx} ({score}) must be between 0 and 100.")
            return

        group = str(row['group']).strip().title()

        if group == 'Formative':
            formative_score += (score * weight) / 100.0
            formative_weight += weight
            if score < 50:
                failed_formatives.append((row['assignment'], score, weight))
        elif group == 'Summative':
            summative_score += (score * weight) / 100.0
            summative_weight += weight
        else:
            print(f"Error: Invalid group '{group}' in row {idx}. Must be 'Formative' or 'Summative'.")
            return

    # Check total weights (60 Formative / 40 Summative)
    if round(formative_weight, 2) != 60.0 or round(summative_weight, 2) != 40.0:
        print(f"Error: Formative weights must total 60 (got {formative_weight}) and Summative weights must total 40 (got {summative_weight}).")
        return

    # Calculate overall percentages and GPA
    formative_pct = (formative_score / 60.0) * 100
    summative_pct = (summative_score / 40.0) * 100

    final_grade = formative_score + summative_score
    gpa = (final_grade / 100.0) * 5.0

    formative_pass = formative_pct >= 50.0
    summative_pass = summative_pct >= 50.0

    # Display Report
    print("\n" + "="*40)
    print("           GRADE EVALUATION REPORT       ")
    print("="*40)
    print(f"Formative Score: {formative_pct:.2f}% ({'PASS' if formative_pass else 'FAIL'})")
    print(f"Summative Score: {summative_pct:.2f}% ({'PASS' if summative_pass else 'FAIL'})")
    print(f"Final Grade:     {final_grade:.2f}%")
    print(f"Calculated GPA:  {gpa:.2f} / 5.0")
    print("-" * 40)

    if formative_pass and summative_pass:
        print("OVERALL STATUS: PASSED 🎉")
    else:
        print("OVERALL STATUS: FAILED ❌")

    if failed_formatives:
        # Sort resubmissions by weight descending
        failed_formatives.sort(key=lambda x: x[2], reverse=True)
        print("\nRecommended Resubmission(s) for Formative Assignments:")
        for name, score, weight in failed_formatives:
            print(f" - {name} (Score: {score}%, Weight: {weight}%)")

def main():
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ").strip()
    data = load_csv_data(filename)
    validate_and_evaluate(data)

if __name__ == "__main__":
    main()
