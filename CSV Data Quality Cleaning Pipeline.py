import csv
import re

input_file = "data/customers_raw.csv"
output_file = "data/cleaned_data.csv"
report_file = "data/data_quality_report.txt"

def validate_name(name):
    """Clean and capitalize names."""
    name = name.strip().title()
    return name if name else None

def validate_email(email):
    """Check for basic email formatting."""
    email = email.strip().lower()
    #Basic regex: non-space chars + @ + non-space chars + . + non-space chars
    if not email:
        return "MISSING"
    if "@" not in email or re.search(r'@.*?\.', email) is None:
        return "INVALID"
    return email

def validate_age(age):
    """Ensure age is a valid integer between 1 and 100."""
    age = age.strip()
    if not age:
        return "MISSING"
    try:
        age = int(age)
        if age < 1 or age >= 100:
            return "INVALID"
        else:
            return age
    except ValueError:
        return "INVALID"

counters = {
    "missing_names": 0,
    "missing_emails": 0,
    "invalid_emails": 0,
    "missing_age": 0,
    "invalid_age": 0,
    "duplicate_records": 0,
    "total_records": 0,
    "clean_records": 0
}

seen_ids = set()

try:
    with open(input_file) as f_in, open(output_file, 'w', newline='') as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)
        writer.writerow(["customer_id", "name", "email", "age"])
        next(reader)

        for row in reader:
            counters["total_records"] += 1

            customer_id = row[0]
            name = validate_name(row[1])  
            email = validate_email(row[2])
            age = validate_age(row[3])

            if not name:
                counters["missing_names"] += 1
                continue
            if email == "MISSING":
                counters["missing_emails"]+=1
                continue
            elif email == "INVALID":
                counters["invalid_emails"]+=1
                continue
            if age == "MISSING":
                counters["missing_age"]+=1
                continue
            elif age == "INVALID":
                counters["invalid_age"]+=1
                continue
            if customer_id in seen_ids:
                counters["duplicate_records"] += 1
                continue

            seen_ids.add(customer_id)
            counters["clean_records"] += 1
            writer.writerow([customer_id, name, email, age])
            print(customer_id, name, email, age)


    dropped_records = counters["total_records"] - counters["clean_records"]

    report_text = f"""
DATA QUALITY REPORT
====================
Total processed: {counters['total_records']}
Clean records:   {counters['clean_records']}
Dropped records: {dropped_records}

Issue Breakdown:
- Missing Names:     {counters['missing_names']}
- Missing Emails:    {counters['missing_emails']}
- Invalid Emails:    {counters['invalid_emails']}
- Missing Age:       {counters['missing_age']}
- Invalid Age:       {counters['invalid_age']}
- Duplicate IDs:     {counters['duplicate_records']}
"""
    print(report_text)

    with open(report_file, 'w') as f_rep:
        f_rep.write(report_text)


except FileNotFoundError:
    print(f"The file {input_file} not found")